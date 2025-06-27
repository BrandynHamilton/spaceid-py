import requests

BASE_URL = "https://nameapi.space.id"

class SpaceIDClient:
    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url

    def resolve_domain(self, domain: str) -> str | None:
        """Resolve a domain name to an address."""
        url = f"{self.base_url}/getAddress"
        resp = requests.get(url, params={"domain": domain})
        data = resp.json()
        return data.get("address") if data.get("code") == 0 else None

    def resolve_address(self, address: str, chain_id: int) -> str | None:
        """Resolve an address to its primary domain name on a specific chain."""
        url = f"{self.base_url}/getName"
        resp = requests.get(url, params={"chainid": chain_id, "address": address})
        data = resp.json()
        return data.get("data", {}).get("name") if data.get("code") == 0 else None

    def resolve_address_multichain(self, address: str, chain_ids: list[int]) -> dict:
        """Resolve an address to domain names across multiple chains."""
        chainlist = ",".join(map(str, chain_ids))
        url = f"{self.base_url}/getDomainNamesByChainIdList"
        resp = requests.get(url, params={"chainlist": chainlist, "address": address})
        result = {}
        if resp.status_code == 200:
            for entry in resp.json().get("data", []):
                chain_id = entry.get("chainID")
                name = entry.get("name")
                if name:
                    result[chain_id] = name
        return result

    def resolve_payment_id(self, payment_id: str, chain_type: str = "evm") -> str | None:
        """Resolve a payment ID (e.g. jerry@binance) to an address."""
        url = f"{self.base_url}/getPaymentIdName/{payment_id}/{chain_type}"
        resp = requests.get(url)
        data = resp.json()
        return data.get("address") if data.get("code") == 0 else None

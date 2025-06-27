# spaceid_py

`spaceid_py` is a lightweight Python SDK for interacting with the [SPACE ID](https://space.id) Web3 Name API. It allows seamless resolution of Web3 domain names, addresses, and payment IDs across multiple chains such as Ethereum, BNB Chain, Arbitrum, and more.

## Features

- Resolve domain name → address
- Resolve address → primary domain name (single-chain)
- Resolve address → domain names across multiple chains
- Resolve payment ID → address (e.g. `jerry@binance`)
- Supports EVM, BTC, Solana, Aptos, Sui, and more via chain type

## Installation

```bash
pip install spaceid_py
```

## Usage

```python
from spaceid_py import SpaceIDClient

sdk = SpaceIDClient()

# 1. Resolve domain to address
print(sdk.resolve_domain("spaceid.bnb"))

# 2. Resolve address to domain (single-chain)
print(sdk.resolve_address("0xb5932a6B7d50A966AEC6C74C97385412Fb497540", 56))  # BNB Chain

# 3. Resolve address to domains on multiple chains
print(sdk.resolve_address_multichain(
    "0x2e552E3aD9f7446e9caB378c008315E0C26c0398",
    [42161, 56, 185]
))

# 4. Resolve Payment ID to address
print(sdk.resolve_payment_id("jerry@binance", "evm"))
```

## API Reference

### `SpaceIDClient(base_url=...)`

| Method                                             | Description                                                 |
| -------------------------------------------------- | ----------------------------------------------------------- |
| `resolve_domain(domain)`                           | Returns address for a given domain (e.g. `spaceid.bnb`)     |
| `resolve_address(address, chain_id)`               | Returns primary domain name for address on a specific chain |
| `resolve_address_multichain(address, chain_ids)`   | Returns domain names across multiple chains                 |
| `resolve_payment_id(payment_id, chain_type='evm')` | Resolves payment ID (e.g. `jerry@binance`) to address       |

## Example Output

```json
{
  "spaceid.bnb": "0xb5932a6B7d50A966AEC6C74C97385412Fb497540",
  "jerry@binance": "0x5bcb636853ab70b873adaf2d9759ca1489669cce"
}
```

## Supported Chains

| Chain            | Chain ID | TLD     |
| ---------------- | -------- | ------- |
| Ethereum Mainnet | 1        | `.eth`  |
| BNB Chain        | 56       | `.bnb`  |
| Arbitrum         | 42161    | `.arb`  |
| Solana           | 900      | `.sol`  |
| Mint             | 185      | `.mint` |
| ... and more     |          |         |

See full list in [SPACE ID API docs](https://docs.space.id/developer-guide/web3-name-api).

## Status Codes

All API calls return a JSON object with:

- `code`: `0` for success, `1` for no result, `-1` for error
- `msg`: status message
- `address` or `name`: returned if available

## License

[MIT License](LICENSE)

## Acknowledgments

- [SPACE ID Team](https://space.id) for their on-chain naming infrastructure
- Built using [SPACE ID Name API](https://docs.space.id/developer-guide/web3-name-api)

---

Need help or want to contribute? PRs welcome.

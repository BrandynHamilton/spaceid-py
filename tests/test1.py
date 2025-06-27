from spaceid_py import SpaceIDClient

if __name__ == "__main__":
    sdk = SpaceIDClient()

    print(F'Supported TLDs: {sdk.supported_tlds}')
    print(F'Supported Chains: {sdk.supported_chains}')
    print(F'TLD to Chain Map: {sdk.tld_chain_map}')

    print("1️⃣ Domain -> Address:")
    print(sdk.resolve_domain("spaceid.bnb"))

    print("2️⃣ Address -> Domain:")
    print(sdk.resolve_address("0xb5932a6B7d50A966AEC6C74C97385412Fb497540", 56))

    print("3️⃣ Multi-chain Resolution:")
    print(sdk.resolve_address_multichain("0x2e552E3aD9f7446e9caB378c008315E0C26c0398", [42161, 56, 185]))

    print("4️⃣ Payment ID -> Address:")
    print(sdk.resolve_payment_id("jerry@binance", "evm"))

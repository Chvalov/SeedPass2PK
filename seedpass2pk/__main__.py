from .solana import get_solana_private_key
from .tron import get_tron_private_key
from .ton import generate_ton_wallet_address, get_ton_private_key


def main():
    mnemonic = input("Enter mnemonic: ").strip()
    passphrase = input("Enter passphrase (leave empty for no passphrase): ").strip()

    # Generate Solana private key and address
    solana_pk, solana_address = get_solana_private_key(mnemonic, passphrase)
    print(f"Solana private key: {solana_pk}")
    print(f"Solana address: {solana_address}")

    # Generate TRON private key and address
    tron_pk, tron_address = get_tron_private_key(mnemonic, passphrase)
    print(f"TRON private key: {tron_pk}")
    print(f"TRON address: {tron_address}")

    # Generate TON private key and address
    ton_pk = get_ton_private_key(mnemonic, passphrase)
    ton_address = generate_ton_wallet_address(ton_pk)
    print(f"TON private key: 0x{ton_pk.hex()}")
    print(f"TON address: {ton_address}")


if __name__ == "__main__":
    main()

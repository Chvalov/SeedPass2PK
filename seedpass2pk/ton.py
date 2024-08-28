from bip_utils import Bip39SeedGenerator, Bip32Slip10Ed25519, Bip32Utils
from nacl.signing import SigningKey
from tonsdk.contract.wallet import Wallets, WalletVersionEnum


def get_ton_private_key(mnemonic: str, passphrase: str) -> bytes:
    # Generate the seed from mnemonic and passphrase
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate(passphrase)

    # Create a context for ed25519 key derivation
    bip32_ctx = Bip32Slip10Ed25519.FromSeed(seed_bytes)

    # Derive path m/44'/607'/0'
    bip32_ctx = bip32_ctx.ChildKey(Bip32Utils.HardenIndex(44))  # purpose (44')
    bip32_ctx = bip32_ctx.ChildKey(Bip32Utils.HardenIndex(607))  # coin_type (607')
    bip32_ctx = bip32_ctx.ChildKey(Bip32Utils.HardenIndex(0))  # account (0')

    # Get the private key in raw bytes
    private_key_bytes = bip32_ctx.PrivateKey().Raw().ToBytes()

    return private_key_bytes


def generate_ton_wallet_address(private_key_bytes):
    # Create a SigningKey object, which automatically handles key pair generation
    signing_key = SigningKey(private_key_bytes)
    public_key_bytes = signing_key.verify_key.encode()

    # The SigningKey object already contains the full 64-byte keypair (private + public)
    full_private_key_bytes = signing_key.encode()

    # Create the wallet using the public and private key
    wallet = Wallets.ALL[WalletVersionEnum.v4r2](public_key=public_key_bytes, private_key=full_private_key_bytes, wc=0)

    # Get the wallet address
    wallet_address = wallet.address.to_string(True, False, False, False)

    return wallet_address


if __name__ == "__main__":
    # HD Wallet
    mnemonic = "sound snap gain emerge above blossom notice used mix fit unable path fruit educate spoon face network strike park boss lumber much essence garden"
    passphrase = "MyB3STP@ssw0rd"

    # Derive the private key
    private_key_bytes = get_ton_private_key(mnemonic, passphrase)
    print(f"TON Wallet Private Key:  0x{private_key_bytes.hex()}")

    # Generate the wallet address
    ton_address = generate_ton_wallet_address(private_key_bytes)
    print(f"TON Wallet Address: {ton_address}")

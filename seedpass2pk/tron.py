from Crypto.Hash import keccak
from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes
from base58 import b58encode_check


def get_tron_private_key(mnemonic: str, passphrase: str) -> tuple[str, str]:
    # Generate the seed from mnemonic and passphrase
    seed_generator = Bip39SeedGenerator(mnemonic)
    seed_bytes = seed_generator.Generate(passphrase)

    # Generate the BIP44 master key for TRON
    bip44_mst_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.TRON)
    bip44_acc_ctx = bip44_mst_ctx.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)

    # Get the private key in bytes format
    private_key = bip44_acc_ctx.PrivateKey().Raw().ToBytes()

    # Generate private key for TRON wallets
    tron_private_key = private_key.hex()

    # Get the public key
    public_key = bip44_acc_ctx.PublicKey().RawUncompressed().ToBytes()[1:]

    # Generate TRON address
    keccak_hash = keccak.new(digest_bits=256)
    keccak_hash.update(public_key)
    address = keccak_hash.digest()[-20:]
    tron_address = b58encode_check(b'\x41' + address).decode()

    return tron_private_key, tron_address


if __name__ == "__main__":
    # Example usage
    mnemonic = "age ring hand armor song panda regular swear unique improve acid lunar"
    passphrase = ""

    private_key, address = get_tron_private_key(mnemonic, passphrase)
    print(f"TRON Private Key: {private_key}")
    print(f"TRON Address: {address}")

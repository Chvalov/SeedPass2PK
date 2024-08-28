from typing import Tuple

from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes, SolAddrEncoder
from base58 import b58encode


def get_solana_private_key(mnemonic: str, passphrase: str) -> tuple[str, str]:
    # Generate the seed from mnemonic and passphrase
    seed_generator = Bip39SeedGenerator(mnemonic)
    seed_bytes = seed_generator.Generate(passphrase)

    # Generate the BIP44 master key for Solana
    bip44_mst_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.SOLANA)
    bip44_acc_ctx = bip44_mst_ctx.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT)

    # Get the private key in bytes format
    private_key = bip44_acc_ctx.PrivateKey().Raw().ToBytes()

    # Get the public key
    public_key = bip44_acc_ctx.PublicKey().RawCompressed().ToBytes()[1:]

    # Generate private recovery key for Solana wallets
    solana_private_key = b58encode(private_key + public_key).decode()

    # Encode the public key to get the Solana address
    address = SolAddrEncoder.EncodeKey(public_key)

    return solana_private_key, address


if __name__ == "__main__":
    # Example usage
    mnemonic = "debate fancy bench arrow morning paper reduce powder pulse blame curtain ancient wrong solar clip same style subway enough infant limb spirit flower marine"
    passphrase = "SeedPass2PK"

    private_key, address = get_solana_private_key(mnemonic, passphrase)
    print(f"Solana Private Key: {private_key}")
    print(f"Solana Address: {address}")

# SeedPass2PK

**SeedPass2PK** is a Python-based tool that generates private keys and addresses for cryptocurrencies using a mnemonic phrase and optional passphrase.

## Features

- **Solana**: Generate private keys and addresses for Solana.
- **TRON**: Generate private keys and addresses for TRON.
- **TON**: Generate private keys and addresses for TON.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Chvalov/SeedPass2PK.git
    cd SeedPass2PK
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Install the project as a module (optional):**

    ```bash
    pip install -e .
    ```

## Usage

### Running as a Command-Line Tool

After installing the package as a module, you can generate private keys and addresses for your cryptocurrency wallet by running the `seedpass2pk` command in the terminal:

```bash
seedpass2pk
```

The script will prompt you to enter a mnemonic phrase and a passphrase (optional). It will then generate and display the private keys and cryptocurrency addresses

### Running the Script Directly

Alternatively, you can run the `main.py` script directly from the project root directory:

```bash
python main.py
```

## Example

Here is an example of how to use the tool:

```bash
seedpass2pk
```

- Enter mnemonic phrase: `debate fancy bench arrow morning paper reduce powder pulse blame curtain ancient wrong solar clip same style subway enough infant limb spirit flower marine`
- Enter passphrase (leave empty for no passphrase): `SeedPass2PK`

Output:
```text
Solana private key: 3wpfsUmMjpGHKV22oyKMi8LmBusZT7ZMqpEecAFPfkqcXex9aAMTjB6ZbSS6CEMkGn3n56S3RfQn5bWUdwYzsbrU
Solana address: CysePuReB7oHzajaFcrQzC3uReNGT39BNnKPQog8D3rk

TRON private key: 811703a8ffcca39c273a5bf4acbb292ba652fe2dc74c54731dd60be0a007a63f
TRON address: TNB3YFyA5KAEkcxxpHnubsE2sRi8U2TwDc

TON private key: 0xb0d0e6f985bcc597febbac6ffb8fc27bf9d60d94df7a3f65a11b2fc886d822b7
TON address: UQA+k8yea9QU4lbFkF2qXEANMc86ghBYtWwkIIFo+hYK4gH3
```
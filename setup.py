from setuptools import setup, find_packages

setup(
    name="seedpass2pk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "bip-utils",
        "base58",
        "tonsdk"
    ],
    entry_points={
        "console_scripts": [
            "seedpass2pk = seedpass2pk.__main__:main"
        ],
    },
)
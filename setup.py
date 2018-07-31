from codecs import open
from os import path
from setuptools import (
    setup,
    find_packages,
)

setup(
    name="web3-gear",
    version="1.0.8",
    license="MIT",
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
    ],
    keywords="thor blockchain ethereum",
    packages=find_packages("."),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=[x.strip() for x in open('requirements')],
    entry_points={
        "console_scripts": [
            "web3-gear=gear.cli:run_server",
        ],
    }
)

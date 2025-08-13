"""
NAG™ - NeuralAgentGenesis
Patent-pending recursive neural network architecture
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nag-system",
    version="0.1.0",
    author="Robert Zemichiel",
    author_email="founder@nag.ai",
    description="Patent-pending neural network where neurons are intelligent agents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/nag-system",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.10",
    install_requires=[
        "numpy>=1.24.0",
        "asyncio>=3.4.3",
        "aiohttp>=3.8.0",
        "pydantic>=2.0.0",
        "prometheus-client>=0.16.0",
        "opentelemetry-api>=1.20.0",
        "redis>=4.5.0",
        "boto3>=1.26.0",  # AWS
        "google-cloud-pubsub>=2.18.0",  # GCP
        "azure-servicebus>=7.11.0",  # Azure
    ],
    extras_require={
        "dev": [
            "pytest>=7.3.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.3.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "nag=nag.cli:main",
        ],
    },
)
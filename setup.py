"""Compatibility entry point for older pip versions without PEP 660 support."""

from setuptools import find_packages, setup


setup(
    name="pdf2htmlex-deb13-py",
    version="0.1.0",
    description="Python interface and Docker builder for high-fidelity PDF to HTML conversion",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages("src"),
    python_requires=">=3.9",
    entry_points={"console_scripts": ["pdf2htmlEX-deb13-py=pdf2htmlex_py.cli:main"]},
)

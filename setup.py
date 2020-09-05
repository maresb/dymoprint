import pathlib

from setuptools import find_packages, setup

from src.dymoprint.constants import VERSION

PROJECT_ROOT = pathlib.Path(__file__).parent

README_TEXT = (PROJECT_ROOT / "README.md").read_text()

setup(
    name="dymoprint",
    version=VERSION,
    description="Linux Software to print with LabelManager PnP from Dymo",
    long_description=README_TEXT,
    long_description_content_type="text/markdown",
    url="https://github.com/computerlyrik/dymoprint",
    author="Sebastian J. Bronner",
    author_email="waschtl@sbronner.com",
    license="Apache License 2.0",
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*",
    install_requires=[
        "appdirs",
        "Pillow==6.2.1",
        "PyQRCode==1.2.1",
        "pyBarcode==0.8b1; python_version=='2.7'",
        "python-barcode==0.9.0; python_version > '3.0'",
    ],
    entry_points={
        "console_scripts": [
            "dymoprint = dymoprint.__main__:main_with_debug",
        ],
    },
    package_dir={
        "": "src",
        "dymoprint_fonts": "data/fonts",
    },
    packages = ["dymoprint", "dymoprint_fonts"],
    package_data={
        "dymoprint_fonts": ["*"],
    },
)

from setuptools import find_packages, setup

__author__ = "spapanik"
__version__ = "0.1.5"
__license__ = "MIT"

PKG_NAME = "tvdb_api_client"
PKG_URL = f"https://github.com/{__author__}/{PKG_NAME}"


def contents(filename):
    with open(filename) as f:
        return f.read()


setup(
    name=PKG_NAME,
    packages=find_packages("src"),
    package_dir={"": "src"},
    version=__version__,
    author=__author__,
    author_email="spapanik21@gmail.com",
    license=__license__,
    description="A python client for TVDB rest API",
    long_description=contents("readme.md"),
    url=PKG_URL,
    download_url=f"{PKG_URL}/tarball/{__version__}",
    python_requires=">=3.6",
    install_requires=["requests>=2.0.0,<2.19.0"],
    keywords=["tvdb", "imdb", "tv series"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
    ],
)

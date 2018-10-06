from setuptools import find_packages, setup

__author__ = "spapanik"
__version__ = "0.1.2"
__license__ = "MIT"
PKG_NAME = "tvdb_api_client"


def contents(filename):
    with open(filename) as f:
        return f.read()


setup(
    name=PKG_NAME,
    packages=find_packages("src"),
    package_dir={"": "src"},
    version=__version__,
    description="A python client for TVDB rest API",
    license=__license__,
    long_description=contents("readme.md"),
    author="Stephanos Papanikolopoulos",
    author_email="spapanik21@gmail.com",
    url=f"https://github.com/{__author__}/{PKG_NAME}",
    download_url="https://github.com/{__author__}/{PKG_NAME}/tarball/{__version__}",
    python_requires=">=3.6",
    install_requires=["requests>=2.0.0,<2.19.0"],
    tests_require=["pytest>=3.0.0,<=3.4.0"],
    keywords=["tvdb", "imdb", "tv series"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
    ],
)

from setuptools import setup

__author__ = 'spapanik'
__version__ = '0.1.0'
__license__ = 'license'
PKG_NAME = 'tvdb_api_client'


def listify(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def contents(filename):
    with open(filename) as f:
        return f.read()

setup(
    name=PKG_NAME,
    packages=[PKG_NAME],
    version=__version__,
    description='A python client for TVDB rest API',
    license=__license__,
    long_description=contents('README.txt'),
    author='Stephanos Papanikolopoulos',
    author_email='spapanik21@gmail.com',
    url=f'https://github.com/{__author__}/{PKG_NAME}',
    download_url='https://github.com/{__author__}/{PKG_NAME}/tarball/{__version__}',
    python_requires='>=3.6',
    install_requires=listify('requirements_install.txt'),
    tests_require=listify('requirements_test.txt'),
    keywords=listify('KEYWORDS.txt'),
    classifiers=listify('CLASSIFIERS.txt'),
)

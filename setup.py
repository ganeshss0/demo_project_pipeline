from setuptools import setup, find_packages

setup(
    name = "census-income",
    version = '0.0.1',
    author = 'Ganesh',
    author_email = 'gs000@proton.me',
    packages = find_packages(),
    install_requires = ['pandas', 'numpy', 'flask']
)
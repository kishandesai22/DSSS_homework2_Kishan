from distutils.core import setup
from setuptools import find_packages

setup(
    name="Kishan",
    version="0.1",
    author="KD",
    author_email="kishan.desai@fau.de",
    packages=find_packages(),
    install_requires=["numpy", "turtles"],
)

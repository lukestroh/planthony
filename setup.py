from setuptools import setup, find_packages
from os import path

__here__ = path.abspath(path.dirname(__file__))

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = open(path.join(__here__, "requirements.txt")).read().strip().split("\n")

setup(
    name="planthony",
    version="0.0.1",
    description="ROS code for connecting Intel RealSense to Kinova Gen3 Arm",
    long_description=long_description,
    author="Luke Strohbehn",
    packages=find_packages(),
    install_requires=install_requires
)
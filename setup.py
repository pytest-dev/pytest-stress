#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os

from setuptools import setup, find_packages


def read(file_name):
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    return codecs.open(file_path, encoding="utf-8").read()


setup(
    name="pytest-stress",
    version="1.0.0",
    author="Imran Mumtaz",
    author_email="iomumtaz@gmail.com",
    maintainer="Imran Mumtaz",
    maintainer_email="iomumtaz@gmail.com",
    license="MIT",
    url="https://github.com/ImXron/pytest-stress",
    description="A Pytest plugin that allows you to loop tests for a user defined amount of time.",
    long_description=read("README.rst"),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.5",
    install_requires=["pytest>=3.6.0"],
    entry_points={"pytest11": ["pytest_stress = pytest_stress.pytest_stress"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
)

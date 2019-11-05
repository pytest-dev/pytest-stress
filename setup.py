#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os

from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
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
    description="A plugin that allows you to loop tests for a user defined amount of time.",
    long_description=read("README.rst"),
    py_modules=["pytest_pytest_stress"],
    python_requires="!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    install_requires=["pytest>=3.5.0"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={"pytest11": ["stress = pytest_stress",],},
)

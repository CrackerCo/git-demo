#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='Git Demo',
    version='0.0.1',
    package_dir={'example':'example'},
    packages=find_packages(),
    install_requires=['flask >= 0.10.1'],
)

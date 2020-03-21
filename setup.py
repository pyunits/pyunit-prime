#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/2/18 15:23
# @Author: Jtyoui@qq.com
from setuptools import setup, find_packages
from distutils.extension import Extension
from os.path import join
import os
from pyunit_prime import __version__, __author__, __description__, __email__, __names__, __url__

dirs = os.path.abspath(os.path.dirname(__file__))

with open(dirs + os.sep + 'README.md', encoding='utf-8') as f:
    long_text = f.read()

ext_modules = [
    Extension('pyunit_prime.prime', [join(dirs, 'pyunit_prime', 'prime.c')])
]

setup(
    name=__names__,
    version=__version__,
    description=__description__,
    long_description=long_text,
    long_description_content_type="text/markdown",
    url=__url__,
    author=__author__,
    author_email=__email__,
    license='MIT Licence',
    packages=find_packages(),
    platforms='any',
    package_data={__names__: ['*.py', '*.c']},
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: C",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux"
    ],
    zip_safe=False,
    ext_modules=ext_modules
)

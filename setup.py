
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='medialpy',
    version='0.0.2',
    description='MEDIcal Abbreviations Lookup in Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AberystwythSystemsBiology/medialpy',
    author='KeironO',
    author_email='keiron.oshea@wales.nhs.uk',
    packages=find_packages(),
    include_package_data=True,
)
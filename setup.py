#!/usr/bin/env python
from setuptools import setup, find_packages
import os

with open('requirements.txt') as fd:
    required = fd.read().splitlines()

setup(name='',
      #Standard variable in build deployment pipeline (used to automatically version the library on each build)
      #version=os.environ['BUILD_BUILDNUMBER'],
      version='0.1',
      description="Data Scientist Coding Challenge",
      url='',
      author='Ian Ormesher',
      author_email='ianormy@gmail.com',
      # install_requires=required,
      # include_package_data=True,
      packages=find_packages())

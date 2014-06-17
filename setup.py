#!/usr/bin/env python
# encoding: utf-8

'''
Created on Oct 29, 2013
@author: mzfa
'''
from setuptools import setup
#from setuptools import find_packages

setup(
    name="tail",
    version="1.0",
    package_dir={'': 'src'},
    packages=['tail'
              ],
    package_data={'': ['*.xml', '*.dll', '*.so']},
    author="mzfa",
    description='agiga endurance test serial port observer and recorder',
    platforms="any"
#     entry_points={
#         "console_scripts": [
#             'prog = getter.main:programming',
#             'fchk = getter.main:finalcheck'
#         ]
#     }
)

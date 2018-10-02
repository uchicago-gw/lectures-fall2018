#!/usr/bin/env python
__usage__ = "setup.py command [--options]"
__description__ = "standard install script"
__author__ = "Reed Essick <reed.essick@gmail.com>, Phil Landry <landryp@uchicago.edu>, Maya Fishbach <mfishbach@uchicago.edu>, Zoheyr Doctor <zdoctor@uchicago.edu>"

#-------------------------------------------------

from distutils.core import setup
import glob
import os.path

setup(
    name = 'lectures-fall2018',
    version = '0.0',
    url = 'https://github.com/uchicago-gw/lectures-fall2018',
    author = __author__,
    author_email = '',
    description = __description__,
    license = 'MIT',
    scripts = [],
    packages = [
        'ucgw_utils',
    ],
    data_files = [],
    requires = [],
)

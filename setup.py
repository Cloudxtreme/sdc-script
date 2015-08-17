#!/usr/bin/env python3
import os
import shutil
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def copyDir(dir):
    # Copy the executable script inside a dir
    if not os.path.exists(dir):
        os.makedirs(dir)
    shutil.copy('./sdc.py', dir + '/sdc')

copyDir('./bin')

setup(
    name='sdc',
    version='v1.0.12',
    description='Python library for access the SysdigCloud API',
    author='Draios Inc. (dba Sysdig) <info@sysdig.com>',
    author_email='info@sysdig.com',
    url='https://sysdig.com/',
    test_suite='tests',
    packages=['sdc', 'sdc.tasks'],
    install_requires=['requests'],
    scripts=['bin/sdc'],
    classifiers=[
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Utilities',
    ]
)

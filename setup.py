#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'ExifRead>=2.1.2'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='image_inspector',
    version='0.3.0',
    description="Simple utility to export exif data from tiff images to csv.",
    long_description=readme + '\n\n' + history,
    author="TNRIS",
    author_email='david.hickman@twdb.texas.gov',
    url='https://github.com/TNRIS/image_inspector',
    packages=[
        'image_inspector',
    ],
    package_dir={'image_inspector':
                 'image_inspector'},
    entry_points={
        'console_scripts': [
            'image-inspector=image_inspector.cli:inspect'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='TNRIS, tif, tiff, exif',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)

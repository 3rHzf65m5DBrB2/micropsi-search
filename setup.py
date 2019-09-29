# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name='micropsi',
    version="0.0.1",
    packages=find_packages(exclude=['tests*']),
    install_requires=[],
    tests_require=['pytest'],
    license='MIT',
    author='Tarek Galal',
    author_email='tare2.galal+github-3rHzf65m5DBrB2@gmail.com',
    description="Find minimum in array",
    long_description="Find minimum in array. Implementation applies a slightly modified binary search to support "
                     "properties of data to be search",
    platforms='any',
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Natural Language :: English',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.5',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Operating System :: MacOS :: MacOS X',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX :: Linux',
                 'Topic :: Software Development :: Libraries :: Python Modules']
)

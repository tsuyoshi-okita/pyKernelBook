#!/usr/bin/env python

"""Setup script for the kernelBook module distribution."""
from distutils.core import setup
#import dataStructure
#from pyKernelBook import __version__

setup(# Distribution meta-data
    name = "pyKernelBook",
    version = '0.1',
    description = "Kernel book examples",
    author = "Tsuyoshi Okita",
    author_email = "tsuyoshi_okita@yahoo.co.jp",
    url = "http://github.com/",
    download_url = "http://github.com/tsuyoshi-okita",
    license = "MIT License",
    packages = ['pyKernelBook.dataStructure','pyKernelBook'],
 
    classifiers=[
        'Development Status :: 1',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        ]
    )

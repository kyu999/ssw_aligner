#!/usr/bin/env python


import numpy as np
from setuptools import find_packages, setup
from setuptools.extension import Extension
from Cython.Build import cythonize


extensions = cythonize([
    Extension("ssw_aligner.ssw_wrapper",
              ["ssw_aligner/ssw_wrapper.pyx",
               "ssw_aligner/_lib/ssw.c"],
              extra_compile_args=['-Wno-error=declaration-after-statement'])
])


setup(name='ssw_aligner',
      version='0.0.7',
      license='MIT',
      description='Python implementation of Striped Smith-Waterman Algorithm',
      long_description='Python implementation of Striped Smith-Waterman Algorithm(one of the local alignment algorithms). Please visit the github page for more details.',
      author="kyu999",
      author_email="kyukokkyou999@gmail.com",
      maintainer="kyu999",
      maintainer_email="kyukokkyou999@gmail.com",
      url='https://github.com/kyu999/ssw_aligner',
      packages=find_packages(),
      ext_modules=extensions,
      classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
      ],
      include_dirs=[np.get_include()]
)

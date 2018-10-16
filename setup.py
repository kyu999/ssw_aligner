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


print np.get_include()
setup(name='ssw_aligner',
      version='0.0.2',
      license='MIT',
      description='',
      author="kyu999",
      author_email="kyukokkyou999@gmail.com",
      maintainer="kyu999",
      maintainer_email="kyukokkyou999@gmail.com",
      url='https://github.com/kyu999/ssw_aligner',
      packages=find_packages(),
      ext_modules=extensions,
      include_dirs=[np.get_include()]
)

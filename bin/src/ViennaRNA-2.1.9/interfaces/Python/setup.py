#!/usr/bin/env python
 
from distutils.core import setup, Extension
import os
import sys
 
old_filename = "RNA.py"
new_filename = "__init__.py"
if os.path.exists(old_filename):
    os.rename(old_filename, new_filename)
 
extra_link_args = ['-fopenmp', '-lstdc++']
extra_compile_args=['-fopenmp']

if sys.platform != 'darwin':
    extra_link_args.append('-s')
 
extension = Extension("_RNA",
                      ["RNA_wrap.c"],
                      include_dirs=['../../H'],
                      libraries=['RNA'],
                      library_dirs=['../../lib'],
                      extra_compile_args=extra_compile_args,
                      extra_link_args=extra_link_args
                      )
 
setup(name="RNA",
      version="2.1.9",
      description="ViennaRNA",
      author="Ivo Hofacker, Institute for Theoretical Chemistry, University of Vienna",
      url="http://www.tbi.univie.ac.at/RNA",
      package_dir = {'RNA':'.'},
      packages = ['RNA'],
      ext_modules=[extension],
      )

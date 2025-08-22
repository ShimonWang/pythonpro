from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize(["cal_pi_compile.py"], annotate=True))
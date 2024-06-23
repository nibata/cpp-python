from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import os
import subprocess
import sys

class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=''):
        super().__init__(name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)

class CMakeBuild(build_ext):
    def run(self):
        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        cmake_args = [
            '-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + extdir,
            '-DPYTHON_EXECUTABLE=' + sys.executable
        ]

        build_temp = os.path.abspath(self.build_temp)
        os.makedirs(build_temp, exist_ok=True)
        old_cwd = os.getcwd()
        try:
            os.chdir(build_temp)
            self.spawn(['cmake', ext.sourcedir] + cmake_args)
            self.spawn(['cmake', '--build', '.'])
        finally:
            os.chdir(old_cwd)

setup(
    name='testpython',
    version='{{VERSION_PLACEHOLDER}}',
    author='Nicolás Bacquet',
    author_email='nibata@gmail.com',
    description='An example package with PyBind11',
    ext_modules=[CMakeExtension('testpython')],
    cmdclass={'build_ext': CMakeBuild},
    zip_safe=False,
)

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import os
import sys
import subprocess
import platform

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
        extdir = os.path.join(extdir, ext.name)  # Ensure the directory is specific to the extension

        cmake_args = [
            f'-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir}',
            f'-DPYTHON_EXECUTABLE={sys.executable}'
        ]

        if platform.system() == 'Windows':
            cmake_args += [
                '-DCMAKE_WINDOWS_EXPORT_ALL_SYMBOLS=TRUE'
            ]
        else:
            cmake_args += [
                '-DCMAKE_POSITION_INDEPENDENT_CODE=TRUE'
            ]

        build_temp = self.build_temp
        os.makedirs(build_temp, exist_ok=True)
        os.makedirs(extdir, exist_ok=True)  # Ensure the target directory exists

        # Log paths for debugging
        print(f"Building extension in: {build_temp}")
        print(f"Placing output in: {extdir}")

        subprocess.check_call(['cmake', ext.sourcedir] + cmake_args, cwd=build_temp)
        subprocess.check_call(['cmake', '--build', '.'], cwd=build_temp)

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

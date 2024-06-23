from setuptools import setup, Extension

setup(
    name='testpython',
    version='{{VERSION_PLACEHOLDER}}',
    author='Nicolás Bacquet',
    author_email='nibata@gmail.com',
    description='An example package with PyBind11',
    ext_modules=[Extension('testpython', ['src/bindings.cpp'])],
    zip_safe=False,
)
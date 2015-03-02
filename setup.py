from setuptools import setup
import sys


dependencies = ['pytest>=2.6']
if sys.version_info < (3, 3):
    dependencies.append('faulthandler')

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='pytest-faulthandler',
    version='0.1',
    py_modules=['pytest_faulthandler'],
    url='https://github.com/nicoddemus/pytest-faulthandler',
    license='MIT',
    install_requires=dependencies, 
    author='Bruno Oliveira',
    author_email='nicoddemus@gmail.com',
    description='py.test plugin that activates the fault handler module for tests',
    long_description=long_description,
    entry_points={
        'pytest11': ['pytest_faulthandler = pytest_faulthandler'],
    },
    keywords='pytest faulthandler',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Testing',
    ]
)

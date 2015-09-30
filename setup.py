from setuptools import setup


with open('README.rst') as f:
    long_description = f.read()

setup(
    name='pytest-faulthandler',
    version='1.0.1',
    py_modules=['pytest_faulthandler'],
    url='https://github.com/pytest-dev/pytest-faulthandler',
    license='MIT',
    install_requires=['pytest>=2.6'],
    author='Bruno Oliveira',
    author_email='nicoddemus@gmail.com',
    description='py.test plugin that activates the fault handler module for tests',
    long_description=long_description,
    extras_require={
        ':python_version=="2.6" or python_version=="2.7"': ['faulthandler'],
    },
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
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Testing',
    ]
)

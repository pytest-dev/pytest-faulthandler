from setuptools import setup


with open('README.rst') as f:
    long_description = f.read()

setup(
    name='pytest-faulthandler',
    use_scm_version=True,
    py_modules=['pytest_faulthandler'],
    url='https://github.com/pytest-dev/pytest-faulthandler',
    license='MIT',
    install_requires=['pytest>=2.6'],
    test_requires=['pytest-mock>=0.6'],
    setup_requires=['setuptools_scm'],
    author='Bruno Oliveira',
    author_email='nicoddemus@gmail.com',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    description='py.test plugin that activates the fault handler module for tests',
    long_description=long_description,
    extras_require={
        ':python_version=="2.7"': ['faulthandler'],
    },
    entry_points={
        'pytest11': ['pytest_faulthandler = pytest_faulthandler'],
    },
    keywords='pytest faulthandler',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Testing',
    ]
)

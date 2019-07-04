from setuptools import setup


with open('README.rst') as f:
    long_description = f.read()

setup(
    name='pytest-faulthandler',
    version="2.0.1",
    url='https://github.com/pytest-dev/pytest-faulthandler',
    license='MIT',
    install_requires=['pytest>=5.0'],
    author='Bruno Oliveira',
    author_email='nicoddemus@gmail.com',
    description='py.test plugin that activates the fault handler module for tests (dummy package)',
    long_description=long_description,
    keywords='pytest faulthandler',
    classifiers=[
        'Development Status :: 6 - Mature',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Testing',
    ]
)

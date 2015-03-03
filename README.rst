===================
pytest-faulthandler
===================

Plugin for pytest that automatically enables the
`faulthandler <http://faulthandler.readthedocs.org/>`_ module during tests.

Inspired by the
`nose faulthandler <https://github.com/schlamar/nose-faulthandler>`_ plugin.

|python| |version| |downloads| |ci|

.. |version| image:: http://img.shields.io/pypi/v/pytest-faulthandler.png
  :target: https://pypi.python.org/pypi/pytest-faulthandler
  
.. |downloads| image:: http://img.shields.io/pypi/dm/pytest-faulthandler.png
  :target: https://pypi.python.org/pypi/pytest-faulthandler

.. |ci| image:: http://img.shields.io/travis/nicoddemus/pytest-faulthandler.png
  :target: https://travis-ci.org/nicoddemus/pytest-faulthandler

.. |python| image:: https://pypip.in/py_versions/pytest-faulthandler/badge.png
  :target: https://pypi.python.org/pypi/pytest-faulthandler/
  :alt: Supported Python versions


Usage
=====

The plugin is always active by default, but you can disable it by passing
``--no-faulthandler`` to ``py.test``.

``faulthandler`` output is redirect to ``stderr``, but if for some reason you need to output it to
a file, you can pass ``--faulthandler-file=XXX`` to ``py.test``. Note that this file will not be
deleted, even if no tests crash. Combining this option with ``pytest_xdist`` will create a file
for each test runner process, and the node id is appended to the filename.


Requirements
============

* Python 2.6+, Python 3.2+
* pytest
* faulthandler


Install
=======

Install using `pip <http://pip-installer.org/>`_:

.. code-block:: console
    
    $ pip install pytest-faulthandler


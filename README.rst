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
`--no-faulthandler` to `py.test`.


Requirements
============

* Python 2.6+, Python 3.2+
* pytest


Install
=======

Install using `pip <http://pip-installer.org/>`_:

.. code-block:: console
    
    $ pip install pytest-faulthandler


===================
pytest-faulthandler
===================

Plugin for pytest that automatically enables the
`faulthandler <https://faulthandler.readthedocs.io/>`_ module during tests.

Inspired by the
`nose faulthandler <https://github.com/schlamar/nose-faulthandler>`_ plugin.

|python| |version| |anaconda| |ci| |appveyor| 

.. |version| image:: http://img.shields.io/pypi/v/pytest-faulthandler.png
  :target: https://pypi.python.org/pypi/pytest-faulthandler

.. |ci| image:: https://api.travis-ci.org/pytest-dev/pytest-faulthandler.svg?branch=master
  :target: https://travis-ci.org/pytest-dev/pytest-faulthandler

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/faf052p56ipp1i4u/branch/master?svg=true
  :target: https://ci.appveyor.com/project/pytestbot/pytest-faulthandler
  
.. |python| image:: https://img.shields.io/pypi/pyversions/pytest-faulthandler.svg
    :target: https://pypi.python.org/pypi/pytest-faulthandler
    
.. |anaconda| image:: https://anaconda.org/conda-forge/pytest-faulthandler/badges/version.svg
    :target: https://anaconda.org/conda-forge/pytest-faulthandler


Usage
=====

The plugin is always active by default, but you can disable it by passing
``--no-faulthandler`` to ``py.test``.

Options:

* ``--faulthandler-timeout=TIMEOUT``: Dump the traceback of all threads if a
  test takes more than TIMEOUT seconds to finish.


Requirements
============

* Python 2.7+, Python 3.4+
* pytest
* faulthandler


Install
=======

Install using `pip <http://pip-installer.org/>`_:

.. code-block:: console
    
    $ pip install pytest-faulthandler

Change Log
==========

Please consult the `CHANGELOG`_.

.. _CHANGELOG: https://github.com/pytest-dev/pytest-faulthandler/blob/master/CHANGELOG.rst

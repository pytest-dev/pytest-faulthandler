===================
pytest-faulthandler
===================


Plugin for pytest that automatically enables the
`faulthandler <https://faulthandler.readthedocs.io/>`_ module during tests.

Inspired by the
`nose faulthandler <https://github.com/schlamar/nose-faulthandler>`_ plugin.

**This plugin is now part of pytest core since pytest 5.0, so users should not install this plugin together with that pytest version.**

**Version 2.0.0 of this package is a dummy package for pytest 5.0 compatibility**.


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
* faulthandler (Python 2.7)


Install
=======

Install using `pip <http://pip-installer.org/>`_:

.. code-block:: console

    $ pip install pytest-faulthandler

Change Log
==========

Please consult the `CHANGELOG`_.

.. _CHANGELOG: https://github.com/pytest-dev/pytest-faulthandler/blob/master/CHANGELOG.rst

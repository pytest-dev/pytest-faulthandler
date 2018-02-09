1.4.1
-----

* Drop support for Python 2.6 and Python 3.3.
* Fix crash when using pytester in default mode with newer pytest versions (`#24`_).
  Thanks `@njsmith`_ for the patch.

.. _#24: https://github.com/pytest-dev/pytest-faulthandler/pull/24

1.4.0
-----

* Botched release, never published to PyPI.

1.3.1
-----

* Fix compatibility with xdist's looponfail mode (`#19`_).
  Patch by `@mhils`_.

.. _#19: https://github.com/pytest-dev/pytest-faulthandler/issues/19

1.3.0
-----

* Now traceback dumping due to an interactive exception is raised (`#14`_).
  Thanks to `@flub`_ for the request.

.. _#14: https://github.com/pytest-dev/pytest-faulthandler/issues/14


1.2.0
-----

* Now traceback dumping due to a timeout is cancelled when entering
  ``pdb``. Thanks to `@The-Compiler`_ for the request (`#12`_).

.. _#12: https://github.com/pytest-dev/pytest-faulthandler/issues/12

1.1.0
-----

* ``--faulthandler-timeout`` option is now properly supported in Python 3+; 
  also a warning is issued instead of an error on platforms without a 
  ``faulthandler.dump_traceback_later`` function (`#8`_).
   
   
.. _#8: https://github.com/pytest-dev/pytest-faulthandler/issues/8   


1.0.1
-----

Release to ensure Python 3.5 compatibility and to provide wheels on PyPI again.


1.0
----

First 1.0 release.

0.2
----

Now properly closing the stream used by the fault handler, thanks to complete 
PR by `@The-Compiler`_. Many thanks!


0.1
----

First public release


.. _@flub: https://github.com/flub
.. _@mhils: https://github.com/mhils
.. _@njsmith: https://github.com/njsmith
.. _@The-Compiler: https://github.com/The-Compiler

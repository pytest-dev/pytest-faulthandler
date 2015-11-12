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


.. _@The-Compiler: https://github.com/The-Compiler

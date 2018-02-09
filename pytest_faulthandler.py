import sys
import os
import pytest
import io


def pytest_addoption(parser):
    group = parser.getgroup('terminal reporting')
    group.addoption(
        '--no-faulthandler', action='store_false', dest='fault_handler',
        default=True, help='Disable faulthandler module.')
    
    group.addoption(
        '--faulthandler-timeout', type=int, dest='fault_handler_timeout',
        metavar='TIMEOUT', default=0,
        help='Dump the traceback of all threads if a test takes '
             'more than TIMEOUT seconds to finish.\n'
             'Not available on Windows.')


def pytest_configure(config):
    if config.getoption('fault_handler'):
        import faulthandler
        try:
            stderr_fileno = sys.stderr.fileno()
        except (AttributeError, io.UnsupportedOperation):
            # python-xdist monkeypatches sys.stderr with an object that is not an actual file.
            # https://docs.python.org/3/library/faulthandler.html#issue-with-file-descriptors
            # This is potentially dangerous, but the best we can do.
            stderr_fileno = sys.__stderr__.fileno()
        stderr_fd_copy = os.dup(stderr_fileno)
        config.fault_handler_stderr = os.fdopen(stderr_fd_copy, 'w')
        faulthandler.enable(config.fault_handler_stderr)
        # we never disable faulthandler after it was enabled, see #3
        
        if config.getoption('fault_handler_timeout') > 0:
            if not timeout_support_available():
                message = 'faulthandler timeout support not available on ' \
                          'this platform'
                config.warn(code='C1', message=message)


def timeout_support_available():
    """Returns True if the current platform/python support faulthandler
    timeout.
    """
    import faulthandler
    return hasattr(faulthandler, 'dump_traceback_later') and \
        hasattr(faulthandler, 'cancel_dump_traceback_later')


@pytest.mark.hookwrapper
def pytest_runtest_protocol(item):
    enabled = item.config.getoption('fault_handler')
    timeout = item.config.getoption('fault_handler_timeout')
    timeout_supported = timeout_support_available()
    if enabled and timeout > 0 and timeout_supported:
        import faulthandler
        stderr = item.config.fault_handler_stderr
        faulthandler.dump_traceback_later(timeout, file=stderr)
        try:
            yield
        finally:
            faulthandler.cancel_dump_traceback_later()
    else:
        yield


def _cancel_traceback_dump():
    """Cancel traceback dumping if timeout support is available.
    """
    if timeout_support_available():
        import faulthandler
        faulthandler.cancel_dump_traceback_later()


@pytest.hookimpl(tryfirst=True)
def pytest_enter_pdb():
    """Cancel any traceback dumping due to timeout before entering pdb.
    """
    _cancel_traceback_dump()


@pytest.hookimpl(tryfirst=True)
def pytest_exception_interact():
    """Cancel any traceback dumping due to an interactive exception being
    raised.
    """
    _cancel_traceback_dump()

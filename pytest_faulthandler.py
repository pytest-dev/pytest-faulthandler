import sys
import os
import pytest


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
        stderr_fd_copy = os.dup(sys.stderr.fileno())
        config.fault_handler_stderr = os.fdopen(stderr_fd_copy, 'w')
        faulthandler.enable(config.fault_handler_stderr)
        # we never disable faulthandler after it was enabled, see #3
        
        if config.getoption('fault_handler_timeout') > 0:
            if sys.platform.startswith('win'):
                msg = '--faulthandler-timeout not available on windows'
                raise pytest.UsageError(msg)            
                

@pytest.mark.hookwrapper
def pytest_runtest_protocol(item):
    enabled = item.config.getoption('fault_handler')
    timeout = item.config.getoption('fault_handler_timeout')
    if enabled and timeout > 0:
        import faulthandler
        stderr = item.config.fault_handler_stderr
        faulthandler.dump_traceback_later(timeout, file=stderr)
        try:
            yield
        finally:
            faulthandler.cancel_dump_traceback_later()
    else:
        yield

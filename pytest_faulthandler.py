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
             'more than TIMEOUT seconds to finish (implies --capture=no).\n'
             'Not available on Windows.')


def pytest_configure(config):
    if config.getoption('fault_handler'):
        import faulthandler
        stderr_fd_copy = os.dup(sys.stderr.fileno())
        config.fault_handler_stderr = os.fdopen(stderr_fd_copy, 'w')
        faulthandler.enable(config.fault_handler_stderr)
        # we never disable faulthandler after it was enabled, see #3
        
        if config.getoption('fault_handler_timeout', default=0) > 0:
            if sys.platform.startswith('win'):
                msg = '--faulthandler-timeout not available on windows'
                raise pytest.UsageError(msg)
            # must disable output capture otherwise the traceback dump
            # will be captured
            capturemanager = config.pluginmanager.getplugin("capturemanager")            
            capturemanager.reset_capturings()
            capturemanager._capturing = capturemanager._getcapture('no')


@pytest.mark.hookwrapper
def pytest_runtest_protocol(item):
    timeout = item.config.getoption('fault_handler_timeout', default=0)
    if timeout > 0:
        import faulthandler
        faulthandler.dump_traceback_later(timeout)
        try:
            yield
        finally:
            faulthandler.cancel_dump_traceback_later()
    else:
        yield

import sys
import os
import faulthandler


def pytest_addoption(parser):
    group = parser.getgroup('terminal reporting')
    group.addoption(
        '--no-faulthandler', action='store_false', dest='fault_handler',
        default=True, help='Disable faulthandler module.')


def pytest_configure(config):
    if config.getoption('fault_handler'):
        stderr_fd_copy = os.dup(sys.stderr.fileno())
        config.fault_handler_stderr = os.fdopen(stderr_fd_copy, 'w')
        faulthandler.enable(config.fault_handler_stderr)


def pytest_unconfigure(config):
    if config.getoption('fault_handler'):
        faulthandler.disable()
        config.fault_handler_stderr.close()
        del config.fault_handler_stderr

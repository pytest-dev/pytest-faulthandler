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
        stderr_copy = os.fdopen(stderr_fd_copy, 'w')
        faulthandler.enable(stderr_copy)


def pytest_unconfigure(config):
    if config.getoption('fault_handler'):
        faulthandler.disable()
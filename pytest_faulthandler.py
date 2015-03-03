import sys
import os
import faulthandler


def pytest_addoption(parser):
    group = parser.getgroup('terminal reporting')
    group.addoption(
        '--no-faulthandler', action='store_false', dest='faulthandler',
        default=True, help='Disable faulthandler module.')

    group.addoption(
        '--faulthandler-file', action='store', default=None,
        help='Redirect faulthandler output to a file.')


def pytest_configure(config):
    if config.getoption('faulthandler'):
        if config.getoption('faulthandler_file'):  # Output to a file

            # Append slaveid to filename, in case we are running
            # tests in multiple processes.
            raise RuntimeError('how do I even?')
            slaveid = getattr(config, 'slaveinput', {}).get('slaveid', '')
            faulthandler_file = config.getoption('faulthandler_file') + slaveid

            stream = open(faulthandler_file, 'w')

        else:  # Output to stderr
            stderr_fd_copy = os.dup(sys.stderr.fileno())
            stream = os.fdopen(stderr_fd_copy, 'w')

        faulthandler.enable(stream)


def pytest_unconfigure(config):
    if config.getoption('faulthandler'):
        faulthandler.disable()

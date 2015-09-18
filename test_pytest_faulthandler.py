import pytest
import sys

pytest_plugins = ['pytester']


def test_enabled(testdir):
    """Test single crashing test displays a traceback."""
    testdir.makepyfile('''
    import faulthandler
    def test_crash():
        faulthandler._sigabrt()
    ''')
    result = testdir.runpytest()
    result.stderr.fnmatch_lines([
        "*Fatal Python error*"
    ])
    assert result.ret != 0


def test_crash_near_exit(testdir):
    """Test that fault handler displays crashes that happen even after
    pytest is exiting (for example, when the interpreter is shutting down).
    """
    testdir.makepyfile('''
    import faulthandler
    import atexit
    def test_ok():
        atexit.register(faulthandler._sigabrt)
    ''')
    result = testdir.runpytest()
    result.stderr.fnmatch_lines([
        "*Fatal Python error*"
    ])
    assert result.ret != 0


def test_disabled(testdir):
    """Test option to disable fault handler in the command line.
    """
    testdir.makepyfile('''
    import faulthandler
    def test_disabled():
        assert not faulthandler.is_enabled()
    ''')
    result = testdir.runpytest('--no-faulthandler')
    result.stdout.fnmatch_lines([
        "*1 passed*"
    ])
    assert result.ret == 0


@pytest.mark.parametrize('enabled', [True, False])
@pytest.mark.skipif(sys.platform.startswith('win'), reason='linux only')
def test_timeout(testdir, enabled):
    """Test option to dump tracebacks after a certain timeout (linux only).
    If falthandler is disabled, no traceback will be dumped.
    """
    testdir.makepyfile('''    
    import time
    def test_timeout():
        time.sleep(2.0)
    ''')
    args = ['--faulthandler-timeout=1']
    if not enabled:
        args.append('--no-faulthandler')
        
    result = testdir.runpytest(*args)
    tb_output = 'most recent call first'
    if sys.version_info[:2] == (3, 3):
        tb_output = 'Thread'
    if enabled:
        result.stderr.fnmatch_lines([
            "*%s*" % tb_output,
        ])
    else:
        assert tb_output not in result.stderr.str()
    result.stdout.fnmatch_lines([        
        "*1 passed*",
    ])
    assert result.ret == 0


@pytest.mark.skipif(not sys.platform.startswith('win'), reason='windows only')
def test_timeout_not_available_windows(testdir):
    """Test that --faulthandler-timeout option on windows shows an
    appropriate error message.
    """
    result = testdir.runpytest('--faulthandler-timeout=1')
    result.stderr.fnmatch_lines([
        "*--faulthandler-timeout not available on windows",
    ])
    assert result.ret != 0

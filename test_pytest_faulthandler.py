import pytest


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
def test_timeout(testdir, enabled):
    """Test option to dump tracebacks after a certain timeout.
    If falthandler is disabled, no traceback will be dump.
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
    if enabled:
        result.stderr.fnmatch_lines([
            "*(most recent call first):",        
        ])
    else:
        assert 'most recent call first' not in result.stderr.str()
    result.stdout.fnmatch_lines([        
        "*1 passed*",
    ])
    assert result.ret == 0	

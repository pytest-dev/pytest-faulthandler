import pytest
import sys
from pytest_faulthandler import timeout_support_available

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
@pytest.mark.skipif(not timeout_support_available(), reason='no timeout support')
def test_timeout(testdir, enabled):
    """Test option to dump tracebacks after a certain timeout (linux only).
    If faulthandler is disabled, no traceback will be dumped.
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


@pytest.mark.skipif(timeout_support_available(), reason='timeout available')
def test_timeout_not_available(testdir):
    """Test that --faulthandler-timeout option on shows a warning on
    platforms that don't support it (#8).
    """
    testdir.makepyfile('''
        def test_dummy():
            pass
    ''')
    result = testdir.runpytest('--faulthandler-timeout=5', '-rw')
    result.stdout.fnmatch_lines([
        '*warnings summary*',
        "*faulthandler timeout support not available on this platform*",
        '*= 1 passed, 1 warnings in *',
    ])
    assert result.ret == 0


@pytest.mark.skipif(not timeout_support_available(), reason='no timeout support')
@pytest.mark.parametrize('hook_name', ['pytest_enter_pdb',
                                       'pytest_exception_interact'])
def test_cancel_timeout_on_hook(mocker, pytestconfig, hook_name):
    """Make sure that we are cancelling any scheduled traceback dumping due
    to timeout before entering pdb (#12) or any other interactive
    exception (#14).
    """
    import faulthandler
    import pytest_faulthandler

    m = mocker.spy(faulthandler, 'cancel_dump_traceback_later')

    # call our hook explicitly, we can trust that pytest will call the hook
    # for us at the appropriate moment
    hook_func = getattr(pytest_faulthandler, hook_name)
    hook_func()
    assert m.call_count == 1

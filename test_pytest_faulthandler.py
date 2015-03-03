pytest_plugins = ['pytester']

def test_enabled(testdir):
    testdir.makepyfile('''
    import faulthandler
    def test_crash():
        faulthandler._sigabrt()
    ''')
    result = testdir.runpytest()
    result.stderr.fnmatch_lines([
        "*Fatal Python error*"
    ])


def test_disabled(testdir):
    testdir.makepyfile('''
    import faulthandler
    def test_disabled():
        assert not faulthandler.is_enabled()
    ''')
    result = testdir.runpytest('--no-faulthandler')
    result.stdout.fnmatch_lines([
        "*1 passed*"
    ])


def test_faulthandler_file(testdir, tmpdir):
    faulthandler_file = tmpdir + '/faulthandler'

    testdir.makepyfile('''
    import faulthandler
    def test_crash():
        faulthandler._sigabrt()
    ''')
    result = testdir.runpytest('--faulthandler-file=%s' % faulthandler_file)
    result.stderr.fnmatch_lines([])

    assert faulthandler_file.readlines()[0] == 'Fatal Python error: Aborted\n'


def test_faulthandler_file_xdist(testdir, tmpdir):
    faulthandler_file = tmpdir + '/faulthandler'

    testdir.makepyfile('''
    import faulthandler
    def test_crash_1():
        faulthandler._sigabrt()
    def test_crash_2():
        faulthandler._sigabrt()
    ''')
    result = testdir.runpytest('-n2', '--faulthandler-file=%s' % faulthandler_file)
    result.stderr.fnmatch_lines([])
    
    # When running with xdist, mutiple files will be created based on slaveid
    faulthandler_file0 = tmpdir + '/faulthandler0'
    assert faulthandler_file0.readlines()[0] == 'Fatal Python error: Aborted\n'

    faulthandler_file1 = tmpdir + '/faulthandler1'
    assert faulthandler_file1.readlines()[0] == 'Fatal Python error: Aborted\n'

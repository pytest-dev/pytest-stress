pytest_plugins = ("pytester",)


def test_help_message(testdir):
    result = testdir.runpytest("--help")
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(
        [
            "stress:",
            "*--delay=DELAY*The amount of time to wait between each test loop.",
            "*--hours=HOURS*The number of hours to loop the tests for.",
            "*--minutes=MINUTES*The number of minutes to loop the tests for.",
            "*--seconds=SECONDS*The number of seconds to loop the tests for.",
        ]
    )


def test_ini_file(testdir):
    testdir.makeini(
        """
        [pytest]
        addopts = --delay=0 --hours=0 --minutes=0 --seconds=0
    """
    )

    testdir.makepyfile(
        """
        import pytest

        @pytest.fixture
        def addopts(request):
            return request.config.getini('addopts')

        def test_ini(addopts):
            assert addopts[0] == "--delay=0"
            assert addopts[1] == "--hours=0"
            assert addopts[2] == "--minutes=0"
            assert addopts[3] == "--seconds=0"
    """
    )

    result = testdir.runpytest("-v")

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(
        ["*::test_ini PASSED*", ]
    )

    # Make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0

from src import __version__


class TestVersion:
    def test_should_get_version(self):
        assert isinstance(__version__, str)

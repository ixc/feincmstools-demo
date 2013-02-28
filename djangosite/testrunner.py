"""
This file is provided as a template for plugging in a custom text runner; the
one defined below does not provide any additional functionality.
"""
from django.test.simple import DjangoTestSuiteRunner
from discover_runner import DiscoverRunner


class CustomTestRunner(DjangoTestSuiteRunner):
    """
    Custom test runner ready for customisation, does not actually provide
    any additional functionality right now.
    """

    def __init__(self, *args, **kwargs):
        # Do custom stuff here
        super(CustomTestRunner, self).__init__(*args, **kwargs)


class UnitTest2TestDiscovery(DiscoverRunner):
    """
    Custom test runner that uses sensible unittest2 test discovery to find our
    test cases in the tests/ project directory.
    """
    pass

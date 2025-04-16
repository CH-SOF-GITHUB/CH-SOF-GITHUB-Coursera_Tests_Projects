import unittest

from TCs import TestCasesPythonOrg


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCasesPythonOrg("test_UpcomingEventsSectionPresentInAboutPage"))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(test_suite())

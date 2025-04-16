import unittest

from HtmlTestRunner import HTMLTestRunner

from TestCases import TestCasesPythonOrg


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCasesPythonOrg("test_UpcomingEventsSectionPresentInAboutPage"))
    return suite


if __name__ == '__main__':
    runner = HTMLTestRunner(verbosity=2, output='report', report_name='report', open_in_browser=True)
    # runner = unittest.TextTestRunner()
    runner.run(test_suite())

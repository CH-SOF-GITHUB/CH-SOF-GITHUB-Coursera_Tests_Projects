import unittest

from HtmlTestRunner import HTMLTestRunner

from TestCasesPOM import TestCases001And002
from TestCasesPOM import TestTC003


def suite():
    suite_tests = unittest.TestSuite()
    suite_tests.addTest(TestCases001And002("test_TC0O1"))  # Test TC001
    suite_tests.addTest(TestCases001And002("test_TC002"))  # Test TC002
    suite_tests.addTest(TestTC003("test_TC003"))  # Test TC003
    return suite_tests


if __name__ == '__main__':
    runner = HTMLTestRunner(
        verbosity=2,
        output='pomReports',
        report_title='Test cases Python Page_Objects_Models Results',
        report_name='rapport html des tests avec pom python.org',
        open_in_browser=True
    )
    runner.run(suite())

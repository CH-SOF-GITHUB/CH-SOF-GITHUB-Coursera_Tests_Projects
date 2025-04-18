import unittest

from HtmlTestRunner import HTMLTestRunner

from TestCasesPOM import TestCases001002003
from TestCasesPOM import TestTC004005


def suite():
    suite_tests = unittest.TestSuite()
    suite_tests.addTest(TestCases001002003("test_TC0O1"))  # Test TC001
    suite_tests.addTest(TestCases001002003("test_TC002"))  # Test TC002
    suite_tests.addTest(TestCases001002003("test_TC003"))  # Test TC003
    suite_tests.addTest(TestTC004005("test_TC004"))  # Test TC004
    suite_tests.addTest(TestTC004005("test_TC005"))
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

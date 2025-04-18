import unittest

from allTestsFirefoxLambdaTest import TestCasesFirefox001002003
from allTestsFirefoxLambdaTest import TestCasesFirefox004005


def suite_firefox():
    suiteChrome = unittest.TestSuite()
    suiteChrome.addTest(TestCasesFirefox001002003("test_TC0O1"))
    suiteChrome.addTest(TestCasesFirefox001002003("test_TC002"))
    suiteChrome.addTest(TestCasesFirefox001002003("test_TC003"))
    suiteChrome.addTest(TestCasesFirefox004005("test_TC004"))
    suiteChrome.addTest(TestCasesFirefox004005("test_TC005"))
    return suiteChrome


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    suite = suite_firefox()
    runner.run(suite)

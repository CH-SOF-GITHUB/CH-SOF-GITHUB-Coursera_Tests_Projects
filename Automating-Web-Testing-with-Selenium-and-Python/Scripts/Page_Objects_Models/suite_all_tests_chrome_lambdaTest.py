import unittest

from allTestsChromeLambdaTest import TestCasesChrome001002003
from allTestsChromeLambdaTest import TestCasesChrome004005


def suite_chrome():
    suiteChrome = unittest.TestSuite()
    suiteChrome.addTest(TestCasesChrome001002003("test_TC0O1"))
    suiteChrome.addTest(TestCasesChrome001002003("test_TC002"))
    suiteChrome.addTest(TestCasesChrome001002003("test_TC003"))
    suiteChrome.addTest(TestCasesChrome004005("test_TC004"))
    suiteChrome.addTest(TestCasesChrome004005("test_TC005"))
    return suiteChrome


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    suite = suite_chrome()
    runner.run(suite)

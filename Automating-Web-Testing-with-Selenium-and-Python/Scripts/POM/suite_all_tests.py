import unittest

from TestCasesPOM import TestCases001002003
from TestCasesPOM import TestTC004005


def suite():
    all_suite = unittest.TestSuite()
    all_suite.addTest(TestCases001002003('test_TC0O1'))
    all_suite.addTest(TestCases001002003('test_TC002'))
    all_suite.addTest(TestCases001002003('test_TC003'))
    #
    all_suite.addTest(TestTC004005('test_TC004'))
    all_suite.addTest(TestTC004005('test_TC005'))

    return all_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    suite = suite()
    runner.run(suite)

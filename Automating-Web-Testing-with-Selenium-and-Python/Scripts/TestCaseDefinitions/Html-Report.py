import logging
import sys
import unittest

import HtmlTestRunner

logging.basicConfig()
log = logging.getLogger("DummyLogger")


class TestStringMethods(unittest.TestCase):
    """ Example test for HtmlRunner. """

    def test_upper(self):
        """ Test where I put warning inside of it """
        log.info('Printing info inside test case')
        log.warning('Printing warn inside test case')
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        log.info('Printing info inside test case')
        log.warning('Printing warn inside test case')
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_error(self):
        """ This test should be marked as error one. """
        raise ValueError

    def test_fail(self):
        """ This test should fail. """
        log.info('Printing info inside test case')
        log.warning('Printing warn inside test case')
        self.assertEqual(1, 2)

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """
        pass


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("DummyLogger").setLevel(logging.INFO)
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='outputFolder', report_title='Dummy report title test'))

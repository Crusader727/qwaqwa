#!/usr/bin/env python2

import sys
import unittest
from tests.main import Main


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(Main),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())

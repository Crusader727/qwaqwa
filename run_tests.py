#!/usr/bin/env python2

import sys
import unittest
from tests.tests import Tests
from tests.suites.tests_send_document import TestsSendDocuments
from tests.suites.tests_send_messages import TestsSendMessages


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(Tests),
    ))
    suite1 = unittest.TestSuite((
        unittest.makeSuite(TestsSendDocuments),
    ))
    suite2 = unittest.TestSuite((
        unittest.makeSuite(TestsSendMessages),
    ))
    result = unittest.TextTestRunner().run(suite)
    result1 = unittest.TextTestRunner().run(suite1)
    result2 = unittest.TextTestRunner().run(suite2)
    
    sys.exit(not result.wasSuccessful() or not result1.wasSuccessful() or not result2.wasSuccessful())
    


#!/usr/bin/env python
#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.

import sys, os
DIR = os.path.abspath(os.path.normpath(os.path.join(__file__,
    '..', '..', '..', '..', '..', 'trytond')))
if os.path.isdir(DIR):
    sys.path.insert(0, os.path.dirname(DIR))

import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_view


class PurchaseInvoiceLineStandaloneTestCase(unittest.TestCase):
    '''
    Test PurchaseInvoiceLineStandalone module.
    '''

    def setUp(self):
        trytond.tests.test_tryton.install_module(
                'purchase_invoice_line_standalone')

    def test0005views(self):
        '''
        Test views.
        '''
        self.assertRaises(Exception, test_view(
            'purchase_invoice_line_standalone'))

def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            PurchaseInvoiceLineStandaloneTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
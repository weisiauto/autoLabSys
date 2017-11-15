#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:37:26 2017

@author: weizy
"""

import unittest

class SimpleTest(unittest.TestCase):
    def test(self):
        self.failUnless(True)

if __name__=='__main__':
    unittest.main()
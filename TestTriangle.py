# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk

@author: Caroline Telma
Updated on September 9 2018

"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangle1(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangle2(self):
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testEquilateralTriangle1(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTriangle2(self):
        self.assertEqual(classifyTriangle(4,4,4),'Equilateral','4,4,4 should be equilateral')

    def testScaleneTriangle1(self):
        self.assertEqual(classifyTriangle(4,5,6),'Scalene','4,5,6 should be scalene')

    def testScaleneTriangle2(self):
        self.assertEqual(classifyTriangle(3,5,7),'Scalene','3,5,7 should be scalene')

    def testIsoscelesTriangle1(self):
        self.assertEqual(classifyTriangle(5,5,9),'Isosceles','5,5,9 should be isosceles')

    def testIsoscelesTriangle2(self):
        self.assertEqual(classifyTriangle(4,4,7),'Isosceles','4,4,7 should be isosceles')

    def testInvalidInput1(self):
        self.assertEqual(classifyTriangle(250,300,-350),'InvalidInput','300,350,-100 should be InvalidInput')

    def testInvalidInput2(self):
        self.assertEqual(classifyTriangle('eight',2,9),'InvalidInput','eight,2,9 should be InvalidInput')

    def testNotATriangle1(self):
        self.assertEqual(classifyTriangle(3,3,7),'NotATriangle','3,3,7 should be NotATriangle')

    def testNotATriangle2(self):
        self.assertEqual(classifyTriangle(2,4,9),'NotATriangle','2,4,9 should be NotATriangle')



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

#!/usr/bin/env python3
# unittest

import unittest


class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)


unittest.main()

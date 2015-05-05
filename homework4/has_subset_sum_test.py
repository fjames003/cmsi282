from itertools import chain, combinations
from has_subset_sum import has_subset_sum
import unittest

class SubsetSumTestCase(unittest.TestCase):
    def test_it(self):
        self.assertTrue(has_subset_sum([], 0))
        self.assertTrue(has_subset_sum([4], 4))
        self.assertFalse(has_subset_sum([4], 8))
        self.assertTrue(has_subset_sum([4, -1], 4))
        self.assertTrue(has_subset_sum([4, -1], 3))
        self.assertTrue(has_subset_sum([4, -1], -1))
        self.assertFalse(has_subset_sum([4, -1], 40))
        self.assertFalse(has_subset_sum([4, -1], -80))

    def test_a_specific_example(self):
        s = [-3, -4, 1, 4]
        for k in (-7, -6, -4, -3, -2, 0, 1, 2, 4, 5):
            self.assertTrue(has_subset_sum(s, k))
        for k in (-10, -9, -8, -5, -1, 3, 6, 7, 8, 9):
            self.assertFalse(has_subset_sum(s, k))

unittest.main()
import sorting as s
import unittest
import random

unsorted_list = [random.randint(1, 20) for _ in range(10)]
expected_sorted_list = sorted(unsorted_list)


class TestSorters(unittest.TestCase):
    def test_bubblesort(self):

        actual_sorted_list = s.bubble_sort(unsorted_list)
        self.assertEqual(expected_sorted_list, actual_sorted_list)

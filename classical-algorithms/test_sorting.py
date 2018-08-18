import sorting as s
import unittest
import random


class TestSorters(unittest.TestCase):

    def test_bubblesort(self):

        unsorted_list = [random.randint(1, 120) for _ in range(100)]
        expected_sorted_list = sorted(unsorted_list)
        bubble_sorted_list = s.bubble_sort(unsorted_list)
        self.assertEqual(expected_sorted_list, bubble_sorted_list)

    def test_mergesort(self):

        unsorted_list = [random.randint(1, 120) for _ in range(100)]
        expected_sorted_list = sorted(unsorted_list)
        merge_sorted_list = s.merge_sort(unsorted_list)
        self.assertEqual(expected_sorted_list, merge_sorted_list)

import unittest
from iterator import *
import random


class TestCollection(unittest.TestCase):
    def test_iterator(self):
        items = []
        items.append(1)
        items.append(2)
        col = Collection(items)
        items_col = []
        for c in col:
            items_col.append(c)
        self.assertEqual(items_col, items)
        items_col = []
        for i in range(len(col)):
            items_col.append(col[i])
        self.assertEqual(items_col, items)

    def test_add(self):
        col = Collection([])
        col.add(1)
        self.assertEqual(col[0], 1)
        self.assertEqual(len(col), 1)
        col.add(2)
        self.assertEqual(col[1], 2)
        self.assertEqual(len(col), 2)

    def test_set_item(self):
        col = Collection([1, 2])
        col[0] = 100
        self.assertEqual(col[0], 100)
        self.assertEqual(col[1], 2)

    def test_delete_item(self):
        col = Collection([1, 2])
        del col[0]
        self.assertEqual(len(col), 1)
        self.assertEqual(col[0], 2)


class TestCombSort(unittest.TestCase):
    def test_sort(self):
        def compare_asc(x, y):
            return x > y
        lst = random.sample(range(1, 50), 10)
        list_sorted = []
        for i in range(len(lst)):
            list_sorted.append(lst[i])
        list_sorted.sort()
        lst = comb_sort(lst, compare_asc)
        self.assertEqual(lst, list_sorted)

        def compare_desc(x, y):
            return x < y
        lst = random.sample(range(1, 50), 10)
        list_sorted = []
        for i in range(len(lst)):
            list_sorted.append(lst[i])
        list_sorted.sort(reverse=True)
        lst = comb_sort(lst, compare_desc)
        self.assertEqual(lst, list_sorted)


class TestFilter(unittest.TestCase):
    def test_filter(self):
        def accepted(i):
            return i > 20
        lst = random.sample(range(1, 50), 20)
        filtered_list = []
        for i in range(len(lst)):
            if lst[i] > 20:
                filtered_list.append(lst[i])
        lst = filter(lst, accepted)
        self.assertEqual(lst, filtered_list)
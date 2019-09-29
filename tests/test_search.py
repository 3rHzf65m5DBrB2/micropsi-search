import unittest

from micropsi import search
from .structs import LessThanableElement, SubscriptableClassWithoutLen, UnscubscriptableClassWithLen


class SearchTest(unittest.TestCase):
    def test_min_search(self):
        # simple comparable ints in list
        self.assertEqual(1, search.min_search([3, 2, 1, 2, 3, 5, 6, 7, 9, 10]))
        # should work also on list of strings
        self.assertEqual("a", search.min_search(["e", "d", "c", "b", "a", "b", "c", "d", "e", "f", "g", "h"]))
        # but also on strings
        self.assertEqual("a", search.min_search("edcbabcdefghijklmnopqrstxz"))
        # generally on any list of elements implementing __lt__
        self.assertEqual(0, search.min_search([LessThanableElement(abs(i)) for i in range(-100, 99)]).val)

    def test_min_search_unsubscriptable_should_fail(self):
        try:
            search.min_search(UnscubscriptableClassWithLen())
            raise AssertionError("should have failed on unsubscriptable data")
        except AssertionError:
            pass

    def test_min_search_no_len(self):
        try:
            search.min_search(SubscriptableClassWithoutLen())
            raise AssertionError("should have failed as data does not providing __len__")
        except AssertionError:
            pass

    def test_min_search_empty_data(self):
        try:
            search.min_search([])
            raise AssertionError("should have failed on empty data")
        except AssertionError:
            pass

    def test_min_search_edge_cases(self):
        # minimum at end of strictly monotonically decreasing list
        self.assertEqual(1, search.min_search([10, 5, 1]))
        # minimum exactly at center of a strictly monotonically decreasing then increasing list
        self.assertEqual(1, search.min_search([100, 1, 2]))
        # minimum at beginning of a strictly monotonically increasing list
        self.assertEqual(1, search.min_search([1, 2, 3]))
        # list containing a single item, that item is the minimum
        self.assertEqual(1, search.min_search([1]))
        # smallest splittable list, minimum at end
        self.assertEqual(1, search.min_search([2, 1]))
        # smallest splittable list, minimum at beginning
        self.assertEqual(1, search.min_search([1, 2]))

    def test_min_search_unexpected_data(self):
        try:
            search.min_search([10, 9, 8, 8, 8, 7, 5, 3, 4, 5, 5, 6, 6, 7, 8, 9, 10, 10, 11])
            raise AssertionError("Should have failed as elements are not strictly monotonically "
                                 "decreasing then increasing")
        except ValueError:
            pass

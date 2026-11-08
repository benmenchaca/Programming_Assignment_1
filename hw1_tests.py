"""CSC 1001 - Programming Assignment 1: student-written unit tests.

Create at least TWO separate, meaningful unit tests for each function.
The sixteen methods below are ONLY PLACEHOLDERS: they are not real tests.

Replace each self.fail(...) with test inputs, a call to the appropriate
hw1 function, and unittest assertions about its expected output.
Use methods like self.assertEqual(...) or self.assertAlmostEqual(...).

IMPORTANT: The initial test failures are intentional until you write tests
and implement the functions in hw1.py. Do not simply delete the tests.
"""

import unittest

import data
import hw1


class TestHomework1(unittest.TestCase):

    # Part 1: vowel_count
    def test_vowel_count_case_insensitive(self):
        # TODO: Arrange inputs, call hw1.vowel_count, and assert the result.
        self.assertEqual(hw1.vowel_count("Hello there"), 4)
        # self.("TODO: write the first unit test for vowel_count")
    

    def test_vowel_count_empty_string(self):
        # TODO: Arrange inputs, call hw1.vowel_count, and assert the result.
        #self.fail("TODO: write the second unit test for vowel_count")
        self.assertEqual(hw1.vowel_count(""), 0)

    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
        # TODO: Arrange inputs, call hw1.short_lists, and assert the result.
        #self.fail("TODO: write the first unit test for short_lists")
        self.assertEqual(hw1.short_lists([[1, 2], [], [33, 2, 0, 1], [0, 0], [5]]), [[1, 2], [0, 0]])

    def test_short_lists_no_matching_lengths(self):
        # TODO: Arrange inputs, call hw1.short_lists, and assert the result.
        #self.fail("TODO: write the second unit test for short_lists")
        self.assertEqual(hw1.short_lists([[0], [3, 7, 4], [], [4, 9, 1, 7]]), [])

    # Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        # TODO: Arrange inputs, call hw1.ascending_pairs, and assert the result.
        #self.fail("TODO: write the first unit test for ascending_pairs")
        self.assertEqual(hw1.ascending_pairs([[2, 1], [4, 3], [6, 5]]), [[1, 2], [3, 4], [5, 6]])

    def test_ascending_pairs_other_lengths_unchanged(self):
        # TODO: Arrange inputs, call hw1.ascending_pairs, and assert the result.
        self.assertEqual(hw1.ascending_pairs([[1, 2], [3, 4, 5], [6]]), [[1, 2], [3, 4, 5], [6]])

    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
        # TODO: Arrange inputs, call hw1.add_prices, and assert the result.
        self.assertEqual(hw1.add_prices(data.Price(3, 50), data.Price(2, 25)), data.Price(5, 75))

    def test_add_prices_with_cents_carry(self):
        # TODO: Arrange inputs, call hw1.add_prices, and assert the result.
        self.assertEqual(hw1.add_prices(data.Price(3, 75), data.Price(2, 50)), data.Price(6, 25))

    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
        # TODO: Arrange inputs, call hw1.rectangle_area, and assert the result.
        self.assertEqual(hw1.rectangle_area(data.Rectangle(data.Point(0, 0), data.Point(3, 4))), 12.0)

    def test_rectangle_area_negative_coordinates(self):
        # TODO: Arrange inputs, call hw1.rectangle_area, and assert the result.
        self.assertEqual(hw1.rectangle_area(data.Rectangle(data.Point(-2, -3), data.Point(1, 1))), 12.0)

    # Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        # TODO: Arrange inputs, call hw1.books_by_author, and assert the result.
        book1 = data.Book(["Author A"], "Book 1")
        book2 = data.Book(["Author B"], "Book 2")
        self.assertEqual(hw1.books_by_author("Author A", [book1, book2]), [book1])

    def test_books_by_author_no_matches(self):
        # TODO: Arrange inputs, call hw1.books_by_author, and assert the result.
        self.assertEqual(hw1.books_by_author("Author C", [data.Book(["Author A"], "Book 1"), data.Book(["Author B"], "Book 2")]), [])

    # Part 7: circle_bound
    def test_circle_bound_square(self):
        # TODO: Arrange inputs, call hw1.circle_bound, and assert the result.
        self.assertEqual(hw1.circle_bound(data.Rectangle(data.Point(0, 0), data.Point(2, 2))), data.Circle(data.Point(1.0, 1.0), 1.4142135623730951))

    def test_circle_bound_non_square_rectangle(self):
        # TODO: Arrange inputs, call hw1.circle_bound, and assert the result.
        self.assertEqual(hw1.circle_bound(data.Rectangle(data.Point(0, 0), data.Point(3, 2))), data.Circle(data.Point(1.5, 1.0), 1.8027756377319946))

    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):
        # TODO: Arrange inputs, call hw1.below_pay_average, and assert the result.
        self.assertEqual(hw1.below_pay_average([data.Employee("Alice", 20), data.Employee("Bob", 30), data.Employee("Charlie", 25)]), ["Alice"])

    def test_below_pay_average_empty_list(self):
        # TODO: Arrange inputs, call hw1.below_pay_average, and assert the result.
        self.assertEqual(hw1.below_pay_average([]), [])

if __name__ == '__main__':
    unittest.main()

"""
Bubble Sort Algorithm with Swap Counter and Unit Tests

This script implements the Bubble Sort algorithm, counts the number
of swaps performed, and includes automated test cases using unittest.

Author: AI-Generated
"""

def bubble_sort_with_swaps(arr):
    """
    Sort a list using the Bubble Sort algorithm and count swaps.

    Parameters
    ----------
    arr : list
        List of integers to be sorted.

    Returns
    -------
    tuple
        (sorted_list, swap_count)
    """
    arr = arr.copy()  # avoid modifying original list
    n = len(arr)
    swap_count = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1

    return arr, swap_count





import unittest

class TestBubbleSort(unittest.TestCase):

    def test_unsorted_list(self):
        """Test sorting an unsorted list."""
        result, swaps = bubble_sort_with_swaps([64, 34, 25, 12, 22, 11, 90])
        self.assertEqual(result, [11, 12, 22, 25, 34, 64, 90])
        self.assertTrue(swaps > 0)

    def test_sorted_list(self):
        """Test that already sorted list requires zero swaps."""
        result, swaps = bubble_sort_with_swaps([1, 2, 3, 4, 5])
        self.assertEqual(result, [1, 2, 3, 4, 5])
        self.assertEqual(swaps, 0)

    def test_reverse_sorted_list(self):
        """Test that reverse sorted list requires maximum swaps."""
        result, swaps = bubble_sort_with_swaps([5, 4, 3, 2, 1])
        self.assertEqual(result, [1, 2, 3, 4, 5])
        self.assertEqual(swaps, 10)

    def test_duplicate_values(self):
        """Test sorting when list contains duplicate values."""
        result, swaps = bubble_sort_with_swaps([3, 3, 2, 1, 1])
        self.assertEqual(result, [1, 1, 2, 3, 3])
        self.assertTrue(swaps > 0)

    def test_single_element(self):
        """Test sorting a list with only one element."""
        result, swaps = bubble_sort_with_swaps([7])
        self.assertEqual(result, [7])
        self.assertEqual(swaps, 0)

    def test_empty_list(self):
        """Test sorting an empty list."""
        result, swaps = bubble_sort_with_swaps([])
        self.assertEqual(result, [])
        self.assertEqual(swaps, 0)




if __name__ == "__main__":
    unittest.main()

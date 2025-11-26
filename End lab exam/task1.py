"""
Bubble Sort Algorithm with Swap Counter

This updated version improves the previous bubble_sort function
by adding a swap counter to measure algorithm efficiency.

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
    n = len(arr)
    swap_count = 0

    for i in range(n):
        for j in range(0, n - i - 1):
          
            if arr[j] > arr[j + 1]:
               
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1

    return arr, swap_count


# Example usage and test cases
if __name__ == "__main__":
    test_list1 = [64, 34, 25, 12, 22, 11, 90]
    sorted_list, swaps = bubble_sort_with_swaps(test_list1)
    print("Original List:", [64, 34, 25, 12, 22, 11, 90])
    print("Sorted List:  ", sorted_list)
    print("Total Swaps:  ", swaps)

    test_list2 = [1, 2, 3, 4, 5]
    sorted_list, swaps = bubble_sort_with_swaps(test_list2)
    print("\nAlready Sorted List:", test_list2)
    print("Sorted Output:      ", sorted_list)
    print("Total Swaps:        ", swaps)

    test_list3 = [5, 4, 3, 2, 1]
    sorted_list, swaps = bubble_sort_with_swaps(test_list3)
    print("\nReverse Sorted List:", test_list3)
    print("Sorted Output:     ", sorted_list)
    print("Total Swaps:       ", swaps)
    test_list4 = []
    sorted_list, swaps = bubble_sort_with_swaps(test_list4)     
    print("\nEmpty List:", test_list4)
    print("Sorted Output:     ", sorted_list)
    print("Total Swaps:       ", swaps)
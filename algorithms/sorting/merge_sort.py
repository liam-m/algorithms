"""
    merge_sort.py

    Implementation of merge sort on a list and returns a sorted list.

    Merge Sort Overview:
    ------------------------
    Uses divide and conquer to recursively divide and sort the list

    Time Complexity: O(n log n)

    Space Complexity: O(n) Auxiliary

    Stable: Yes

    Psuedo Code: CLRS. Introduction to Algorithms. 3rd ed.

"""


def merge(left, right):
    if not (left and right):
        return left+right
    elif left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    else:
        return [right[0]] + merge(left, right[1:])


def sort(seq):
    if len(seq) <= 1:
        return seq

    middle = int(len(seq) / 2)
    left = sort(seq[:middle])
    right = sort(seq[middle:])
    return merge(left, right)

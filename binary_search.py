"""
It is used to find an item from a sorted list of items.
It divides the list in half and checks which half the item is in.
The process is repeated on the second half, until the item is found or it is evident that it
does not exist in the list.
"""

def binary_search(arr, x):
    """
    Perform binary search on a sorted list to find the index of a give item.

    :param arr: A sorted list of integers
    :param x: item to search for
    :return: The index of 'x' in 'arr', or -1 if x is not in 'arr'
    """

    # set initial bounds of search
    left, right = 0, len(arr) - 1
    
    # repeat until bounds are crossed
    while left <= right:
        # calculate the index of the middle element in the current portion of list
        mid = (left + right) // 2

        # check if the middle item is the one we are searching for
        if arr[mid] == x:
            return mid

        # If the item is greater than the middle element, search in the right half
        elif arr[mid] < x:
            left = mid + 1

        # if the item is less than the middle element, search in the left half
        else:
            right = mid - 1


    return -1




print("Item is found at index:",binary_search(arr=[1,3,5,7], x=5))
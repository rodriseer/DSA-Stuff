"""
this code will demonstrate binary search
list = the list we are searching for
target = value of the integer, string we are looking for

The time complexity of binary search is O(logn).
This is much more efficient than the linear time O(n), 
especially for large values of n. For example, if the array has 1000 elements

"""

# binary serach break down the list into smaller sections
def binary_search(list, target):

    """
    first: variable to indicat first positon in the list
    last: last position in the list
    the -1 is to inidcate the actual total length of the list, since the index starts at 0
    """
    first = 0
    last = len(list)-1

    # use a while loop
    # this algorithm will run until first is less or equal to the last number
     
    while first <= last:
        # calculate midpoint from the list
        # binary search are known to do this
        # floor division opearator, so it is rounded to the nearest integer
        midpoint = (first + last)//2
        
        # best case scenario, the midpoint is the target
        if list[midpoint] == target:
            return midpoint
        # target less than midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None

# return print result
def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found!")

numbers = [1,2,3,4,5,6,7,8,9,10]

# passing the list and the target value being search
result = binary_search(numbers, 3)
verify(result)












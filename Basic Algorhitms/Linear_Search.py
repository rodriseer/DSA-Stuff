"""
this code will demonstrate linear search
list = the list we are searching for
target = value of the integer, string we are looking for

The Big-O notation for a linear search algorithm is O(N), 
which means that the algorithm's worst-case runtime decreases linearly as the input size increases. 
This makes the algorithm less efficient for large data inputs.

"""

def linear_search(list, target):
    """
    Returns the position of the index position of the target
    else returns None
    """
    # use a for loop
    # iterate through the list, starting at 0 until end of the total list range
    for i in range(0, len(list)):
        # if value at i matches the target then..
        if list[i] == target:
            return i
    return None

# return print result
def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found!")

numbers = [1,2,3,4,5,6,7,8,9,10]

# passing the list and the target value being search
result = linear_search(numbers, 5)
verify(result)
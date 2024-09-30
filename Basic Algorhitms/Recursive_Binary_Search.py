"""
recursive binary search is a funtion that calls itself to perform same operation
its a big looper, basically, or just recursion
everytime it performs a recursion, the list get narrower depending if its less or more util there are no less numbers but the target
Time compexity: O(log n)
The time complexity of binary searches is more efficient than linear search
"""

# takes a list and a target (the value we are looking for)
def recursive_binary_search(list,target):
    # if the list is empty return false
    if len(list) == 0:
        return False
    # if its not empty then else
    else:
        # the midpoint of the list is the length of list floored by 2
        midpoint = (len(list)) // 2
        # if its the midpoint the target return true
        if list[midpoint] == target:
            return True
        else:
            # if its less than the target then
            if list[midpoint] < target:
                # so if it is less, then call back the function with a new list
                # the new list is the list starting at midpoint +1 until the end, the target will also be defined
                return recursive_binary_search(list[midpoint+1:], target)
            # if its greater then
            else:
                # same thing as above, te only difference is that it will start from the beggining of the midpoint list and going until the end
                return recursive_binary_search(list[:midpoint], target)

def verify(result):
    print("Target found", result)

numbers = [1,2,3,4,5,6,7,8]
result = recursive_binary_search(numbers, 12)
verify(result)

result = result = recursive_binary_search(numbers, 4)
verify(result)













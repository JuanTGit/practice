"""
lst[left], lst[right] = lst[right], lst[left]
Continue to swap until the left index is greater than the right index
"""
#Create an inplace function.
def reverse_inplace(lst):
    # Create pointers for our left and right indices.
    left = 0
    # We do len(lst) - 1 because we want to know when they pass. If we do - 1 we don't know how long the list is.
    right = len(lst) - 1
    # While the left index is less than the right index, continue the loop.
    while left < right:
        # While our function runs we will swap our left and right indices.
        lst[left], lst[right] = lst[right], lst[left]
        # Continue to increase the left and decrease the right to tell when they have passed.
        left += 1
        right -= 1
    return lst


random_lst = [5, 10, 4, 20, 25, 30, 35, 6, 45, 50]
print(random_lst)
print(reverse_inplace(random_lst))
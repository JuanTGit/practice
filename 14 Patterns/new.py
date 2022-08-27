from typing import Counter


def longestNiceSubstring(s):
    if len(s) < 2:
        return ''

    result = ''
    
    l = 0
    r = 1
    
    while l < len(s) - 1:
        if s[l].lower() == s[r].lower():
            result += s[l]
            l += 1
        else:
            l += 1
            r += 1
    return result

new_string = "Bb"
# print(longestNiceSubstring(new_string))

# ========================================================

# Find the shortest subarray of k:


def shortestSub(arr, k):
    # Track out min value
    min_length = float('inf')
    print(min_length)
    # The current range and sum of our sliding window
    l = 0
    r = 0
    current_sum = 0

    # Extend the sliding window until our criteria is met
    while r < len(arr):
        current_sum = current_sum + arr[r]
        r = r + 1

        # Then contract the sliding window until it
        # no longer meets our condition
        while l < r and current_sum >= k:
            current_sum = current_sum - arr[l]
            l = l + 1

            # Update the min_length if this is shorter
            # than the current min
            min_length = min(min_length, r - l + 1)
            
    return min_length


# arr1 = [1, 2, 3, 4, 5, 6]
# k1 = 7

# print(shortestSub(arr1, k1))



# name = 'Juan Tejeda'

# print(range(len(name)))

"""
HOW TO IDENTIFY WHEN TO USE A SLIDING WINDOW:
    The problem input is a linear data structure such as a linked list, array, or string.

    Youre asked to find the longest/shortest substring, subarray, or a desired value.

Common problems you use the sliding window pattern with:

    Maximum sum subarray of size K (easy)
    Longest substring with K distinct characters (medium)
    String anagrams (hard)

"""

# given a word w and some text t, 
# find out whether w is in t
w = "nest"
t = "built a nest"

def findWord(w,t):
    t_list = t.split(" ")
    print(t_list)
    return w in t_list

# print(findWord(w,t))
#=========================================================================
def findSliding(w,t):
    # Index pointers
    l = 0
    r = 1
    # While right index is less than the length of our sentence
    while r < len(t):
        # 
        if t[r] == " " or r == len(t)-1:
            if w == t[l:r]:
                return True
            l = r + 1
            r = l + 1
        else:
            r += 1
    return False


# print(findSliding(w,t))
#=========================================================================
# Length of longest substring
"""
Given a string s, find the length of the longest substring without repeating characters.
-------------------------------------------------------
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
-------------------------------------------------------
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
def lengthOfLongestSubstring(a_list):
    # Keeping track of our longest string, left index, and dictionary for letters seen.
    longest = 0
    left = 0
    seen = {}
    # Iterate through the range of the list. Because a string is not iterable use range.
    for i in range(len(a_list)):
        # If the value in our index is in seen execute.
        if a_list[i] in seen:
            # Update our left pointer
            left = max(seen[a_list[i]], left)
        longest = max(longest, i - left + 1)
        seen[a_list[i]] = i + 1
    return longest
#=========================================================================
def longestSub(string):
    longest = 0
    left = 0
    seen = {}
    for i in range(len(string)):
        if string[i] in seen:
            left = seen[string[i]]
            print(f'Left: {left}')
            print(f'Seen: {seen}')
        seen[string[i]] = i + 1
        print(f'Seen First Time: {seen}')

a = "abccaabbbc"
# print(longestSub(a))

#========================================================================
def longestSS(string):
    longest = 0
    left = 0
    right = 0
    seen = {}
    while right < len(string) - 1:
        if string[right] in seen:
            left = seen[string[right]]
        longest = right - left + 1
        seen[string[right]] = right + 1
    return longest

#========================================================================
def fixed_sliding_window(arr, k):
    curr_subarray = sum(arr[:k])
    result = [curr_subarray]

    for i in range(1, len(arr)-k+1):
        curr_subarray = curr_subarray - arr[i-1]
        curr_subarray = curr_subarray + arr[i+k-1]

        result.append(curr_subarray)

    return result


# print(fixed_sliding_window([2, 4, 6, 7, 9, 3, 5], 3))

#========================================================================

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

# ============================================================

# Find the maximum sum in k amount:

# Example:

# arr = [2, 3, 5, 7, 10, 1, 4] k = 3
# output = 22


# Bubble sort grab last 3
def bubbleMax(arr, k):
    if k < 1:
        return ''

    isSorted = False

    while not isSorted:
        isSorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                isSorted = False
    return sum(arr[k+1:])


arr1 = [2, 3, 5, 7, 10, 1, 4]

# print(bubbleMax(arr1, 3))

# ============================================================
# Sliding Window
def slidingMax(arr, k):
    output = []
    l = 0
    r = 0
    total = 0
    while r < len(arr):
        for i in range(len(arr[:k])):
            total += arr[i]
            r += 1
            l += 1
    return total

# print(slidingMax(arr1, 3))

# =============================================================

# 2379. Minimum Recolors to Get K Consecutive Black Blocks
# Easy

# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

# You are also given an integer k, which is the desired number of consecutive black blocks.

# In one operation, you can recolor a white block such that it becomes a black block.

# Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

# Example 1:

# Input: blocks = "WBBWWBBWBW", k = 7
# Output: 3
# Explanation:
# One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
# so that blocks = "BBBBBBBWBW". 
# It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
# Therefore, we return 3.

# Example 2:

# Input: blocks = "WBWBBBW", k = 2
# Output: 0
# Explanation:
# No changes need to be made, since 2 consecutive black blocks already exist.
# Therefore, we return 0.



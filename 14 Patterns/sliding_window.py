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


print(fixed_sliding_window([2, 4, 6, 7, 9, 3, 5], 3))
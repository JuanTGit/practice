# 347. Top K Frequent Elements
# Medium

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

nums = [1,1,1,1,2,2,3]; k = 2

def topKFrequent(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = count.get(n, 0) + 1
    for key, val in count.items():
        freq[val].append(key)
    
    res = []
    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

    # print(freq)
    # print(count)

# print(topKFrequent(nums, k))

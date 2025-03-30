"""
Longest peak of an array (strictly increasing)

sliding window?
"""
array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

def longestPeak(array):
    if len(array) < 3:
        return 0
    
    longest = 0
    
    for i in range(1, len(array) - 1):  # Start from index 1 and go up to the second last element
        # Check if 'array[i]' is the peak
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            left = i - 1
            right = i + 1
            
            # Expand left while the sequence is strictly increasing
            while left >= 0 and array[left] < array[left + 1]:
                left -= 1
            
            # Expand right while the sequence is strictly decreasing
            while right < len(array) and array[right] < array[right - 1]:
                right += 1
            
            # Calculate the length of the peak
            peak_length = right - left - 1
            longest = max(longest, peak_length)
    
    return longest

print(longestPeak(array))
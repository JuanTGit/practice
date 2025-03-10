nums = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]

def longestRange(arr):
    bestRange = []
    longestLength = 0
    visited = {}

    for num in arr:
        visited[num] = True
    for num in arr:
        if not visited[num]:
            continue
        visited[num] = False
        currentLength = 1
        left = num - 1
        right = num + 1
        while left in visited:
            visited[left] = False
            currentLength += 1
            left -= 1
        while right in visited:
            visited[right] = False
            currentLength += 1
            right += 1
        if currentLength > longestLength:
            longestLength = currentLength
            bestRange = [left + 1, right - 1]
    return bestRange
    
print(longestRange(nums))
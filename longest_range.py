nums = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]

def longestRange(array):
    bestRange = []
    longestCount = 0
    visited = {}

    for num in array:
        visited[num] = True
    for num in array:
        if not visited[num]:
            continue
        visited[num] = False
        currentCount = 0
        left = num - 1
        right = num + 1
        while left in visited:
            visited[left] = False
            currentCount += 1
            left -= 1
        while right in visited:
            visited[right] = False
            currentCount += 1
            right += 1
        if currentCount > longestCount:
            longestCount = currentCount
            bestRange = [left + 1, right - 1]
    return bestRange

print(longestRange(nums))
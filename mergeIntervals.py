# Problem: Merge Intervals
# Prompt:
# You are given a list of intervals intervals, where each interval is represented as a list [start, end]. 
# Your task is to merge all overlapping intervals and return the list of merged intervals in ascending order of their starting times.
# Example:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, they are merged into [1,6].

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] overlap, so they are merged.

# Constraints:
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= intervals[i][0] <= intervals[i][1] <= 10^4
intervals = [[1,3],[2,6],[8,10],[15,18]]

def merge_intervals(intervals):
	if not intervals: 
		return []
	intervals.sort(key=lambda x: x[0])
	
	merged = []

	for i in intervals:
		
		if not merged or merged[-1][1] < i[0]:
			merged.append(i)
		else:
			merged[-1][1] = max(merged[-1][1], i[1])

		print(f'Merged[-1]: {merged[-1]}')
		print(f'Merged[-1][1]: {merged[-1][1]}')
	return merged


print(merge_intervals(intervals))

	
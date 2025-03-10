# 2001. Number of Pairs of Interchangeable Rectangles
# Medium
# You are given n rectangles represented by a 0-indexed 2D integer array rectangles, where rectangles[i] = [widthi, heighti] denotes the width and height of the ith rectangle.

# Two rectangles i and j (i < j) are considered interchangeable if they have the same width-to-height ratio. More formally, two rectangles are interchangeable if widthi/heighti == widthj/heightj (using decimal division, not integer division).

# Return the number of pairs of interchangeable rectangles in rectangles.

# Example 1:

# Input: rectangles = [[4,8],[3,6],[10,20],[15,30]]
# Output: 6
# Explanation: The following are the interchangeable pairs of rectangles by index (0-indexed):
# - Rectangle 0 with rectangle 1: 4/8 == 3/6.
# - Rectangle 0 with rectangle 2: 4/8 == 10/20.
# - Rectangle 0 with rectangle 3: 4/8 == 15/30.
# - Rectangle 1 with rectangle 2: 3/6 == 10/20.
# - Rectangle 1 with rectangle 3: 3/6 == 15/30.
# - Rectangle 2 with rectangle 3: 10/20 == 15/30.
# Example 2:

# Input: rectangles = [[4,5],[7,8]]
# Output: 0
# Explanation: There are no interchangeable pairs of rectangles.
 

# Constraints:

# n == rectangles.length
# 1 <= n <= 105
# rectangles[i].length == 2
# 1 <= widthi, heighti <= 105

rectangles = [[4,8],[3,6],[10,20],[15,30]]

def interchangeableRectangles(rectangles):
	count = 0

	for curr in range(len(rectangles)):
		ratio = rectangles[curr][0] / rectangles[curr][1]

		for check in range(curr + 1, len(rectangles)):
			if rectangles[check][0] / rectangles[check][1] == ratio:
				count += 1


	return count

# print(interchangeableRectangles(rectangles))

def interchangeableRectangles2(rectangles):
	count = {}
	res = 0

	for w, h in rectangles:
		count[w / h] = count.get(w / h, 0) + 1

	for c in count.values():
		res += (c * (c - 1)) // 2

	return res


interchangeableRectangles2(rectangles)
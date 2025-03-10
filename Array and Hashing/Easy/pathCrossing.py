# 1496. Path Crossing
# Easy
# Topics
# Companies
# Hint
# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively.
# You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

# Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

# Example 1:

# Input: path = "NES"
# Output: false
# Explanation: Notice that the path doesn't cross any point more than once.
# Example 2:

# Input: path = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice.


def isPathCrossing(path):
	crossedPositions = set()
	currentPosition = [0, 0]
	crossedPositions.add(tuple(currentPosition))

	for pos in path:
		if pos == "N":
			currentPosition[1] += 1
			if tuple(currentPosition) in crossedPositions:
				return True
			crossedPositions.add(tuple(currentPosition))
		elif pos == "E":
			currentPosition[0] += 1
			if tuple(currentPosition) in crossedPositions:
				return True
			crossedPositions.add(tuple(currentPosition))
		elif pos == "S":
			currentPosition[1] -= 1
			if tuple(currentPosition) in crossedPositions:
				return True
			crossedPositions.add(tuple(currentPosition))
		elif pos == "W":
			currentPosition[0] -= 1
			if tuple(currentPosition) in crossedPositions:
				return True
			crossedPositions.add(tuple(currentPosition))	
	return False


print(isPathCrossing("NES"))
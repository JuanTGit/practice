matrix = [[0,1,1,1,1],
		  [1,1,1,1,1],
		  [0,1,1,1,1],
		  [0,1,1,1,1],
		  [1,1,1,0,1],
		  [0,0,1,0,1]]

def largest_square(matrix):

	n = len(matrix)
	m = len(matrix[0])

	dp = [[0] * m for _ in range(n)]
	print(dp)
	max_side = 0

	for i in range(n):
		for j in range(m):
			if matrix[i][j] == 1:
				if i == 0 or j == 0:
					dp[i][j] = 1  # Edge rows/cols
				else:
					dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
				max_side = max(max_side, dp[i][j])
	return max_side


print(largest_square(matrix))
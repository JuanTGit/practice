grid = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

for row in range(len(grid)):
    # print(grid[row])
    for col in range(len(grid[row])):
        # print(grid[row][col])
        # print(col)
        print(row, col, grid[row][col])
    print('end row')
        
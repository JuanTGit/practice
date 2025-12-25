class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMatrix = [[0] * (COLS + 1) for r in range(ROWS + 1)]

        for r in ROWS:
            prefix = 0
            for c in COLS:
                prefix += matrix[r][c]
                above = self.sumMatrix[r][c+1]
                self.sumMatrix[r+1][c+1] = prefix + above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        pass










def testGrid(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    sumMatrix = [[0] * (COLS + 1) for r in range(ROWS + 1)]

    for r in range(ROWS):
        prefix = 0
        for c in range(COLS):
            prefix += matrix[r][c]
            above = sumMatrix[r][c+1]
            sumMatrix[r+1][c+1] = prefix + above

    print(sumMatrix)


print(testGrid([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]))
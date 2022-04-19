

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        pos_i = []
        pos_j = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    pos_i.append(i)
                    pos_j.append(j)
        
        for i in range(m):
            for j in range(n):
                if i in pos_i or j in pos_j:
                    matrix[i][j] = 0
        return matrix

matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(Solution().setZeroes(matrix))

#matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
#print(Solution().setZeroes(matrix))
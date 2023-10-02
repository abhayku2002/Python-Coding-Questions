'''
Make Matrix Beautiful

A beautiful matrix is a matrix in which the sum of elements in each row and column is equal.
Given a square matrix of size NxN. Find the minimum number of operation(s) that are required to make the matrix beautiful. 
In one operation you can increment the value of any one cell by 1.

Input:
N = 2
matrix[][] = {{1, 2},
              {3, 4}}
Output: 
4
Explanation:
Updated matrix:
4 3
3 4
1. Increment value of cell(0, 0) by 3
2. Increment value of cell(0, 1) by 1
Hence total 4 operation are required.

Input:
N = 3
matrix[][] = {{1, 2, 3},
              {4, 2, 3},
              {3, 2, 1}}
Output: 
6
Explanation:
Number of operations applied on each cell are as follows:
1 2 0
0 0 0
0 1 2
Such that all rows and columns have sum of 9.

'''

class Solution:
    def findMinOpeartion(self, matrix, n):
        row_sums = list(map(sum, matrix))
        max_row = max(row_sums)
        col_sums = list(map(sum, zip(*matrix)))
        max_col = max(col_sums)
        max_sum = max(max_row, max_col)
        changes = sum(max_sum - row_sum for row_sum in row_sums)
        return changes

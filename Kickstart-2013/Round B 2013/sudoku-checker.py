import math
import numpy as np

def column(matrix: list, i: int):
  return [row[i] for row in matrix]

#submatrix indexes are 1-indexed and work like this for N=3
# 1 2 3
# 4 5 6
# 7 8 9
def flatSubMatrix(matrix: list, N: int, i: int):
  # This fuction converts a submatrix to a flat array
  res = []
  for r in range(N):
    subRow=np.array(matrix)[r+math.floor((i-1)/N)*N:r+math.floor((i-1)/N)*N+1, ((i-1)%N)*N :((i-1)%N)*N +N]
 
    res.append(*subRow.tolist())
  return np.array(res).flatten()
   

def checkSudoku(sudoku: list, N:int):
  sorted = list(range(1,N*N+1)) #[1,2,..,N^2]

  #Check Rows
  for r in range(N*N):
    row = sudoku[r].copy()
    row.sort()
    if(sorted != row):
      return "No"

  #Check Cols
  for c in range(N*N):
    col = column(sudoku, c).copy()
    col.sort()
    if(sorted != col):
      return "No"

  #Check SubMatrices of (N*N)
  for subMIndex in range(1,N*N+1):
    subMatrix = list(flatSubMatrix(sudoku,N,subMIndex))
    subMatrix.sort()
    if(sorted != subMatrix):
      return "No"

  
  return "Yes"

t = int(input())
for i in range(t):
  N = int(input())
  sudoku = []
  for k in range(N*N):
    row = list(map(int, input().split()))
    sudoku.append(row)
  ans= checkSudoku(sudoku, N)
  print(f"Case #{i+1}: {ans}")
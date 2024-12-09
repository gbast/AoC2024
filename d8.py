import numpy as np
import re
from math import gcd

# Open the file in read mode
with open("d8.txt", "r") as file:
    # Read all lines from the file
    lines = file.readlines()

# Strip whitespace characters like '\n' and print each line
input_data = [line.strip() for line in lines]

matrix = np.array([list(line) for line in input_data])
for r in matrix:
    print(r)
    
# Dimensions of the matrix
rows, cols = matrix.shape
resm=np.full_like(matrix,'.')
for row in range(rows):
    for col in range(cols):
    
        if matrix[row][col] != '.' and matrix[row][col] != '#':
            
            for r in range(rows):
                for c in range(cols):
                    if (r,c) == (row,col):
                        continue
                    if matrix[r][c] == matrix[row][col]:
                       
                            if (2*row-r) in range(0,rows) and (2*col-c) in range(0,cols):
                                resm[2*row-r][2*col-c] ='#'    
                            if (2*r-row) in range(0,rows) and (2*c-col) in range(0,cols):
                                resm[2*r-row][2*c-col] ='#'    
print()
for r in resm:
    print(r)

cnt = 0
for row in range(rows):
    for col in range(cols):
        cnt+=1 if resm[row][col]=='#' else 0
        
print()
print(f'cnt=',cnt)

resm2=np.full_like(matrix,'.')
for row in range(rows):
    for col in range(cols):
    
        if matrix[row][col] != '.' and matrix[row][col] != '#':
            
            for r in range(rows):
                for c in range(cols):
                    if (r,c) == (row,col):
                        continue
                    if matrix[r][c] == matrix[row][col]:
                        dr = r - row
                        dc = c - col
                        g = gcd(abs(dr), abs(dc))
                        ur = dr//g
                        uc = dc//g
                        
                        i=0
                        while True:
                            ir,ic=row+i*ur,col+i*uc
                            
                            if ir in range(0,rows) and ic in range(0,cols):
                                resm2[ir][ic] ='#'
                                i +=1    
                            else:
                                break
                        i=-1
                        while True:
                            ir,ic=row+i*ur,col+i*uc
                            
                            if ir in range(0,rows) and ic in range(0,cols):
                                resm2[ir][ic] ='#'
                                i -=1    
                            else:
                                break
print()
for r in resm2:
    print(r)
cnt = 0
for row in range(rows):
    for col in range(cols):
        cnt+=1 if resm2[row][col]=='#' else 0
        
print()
print(f'cnt=',cnt)
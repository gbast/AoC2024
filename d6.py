import numpy as np
import re
from copy import copy, deepcopy

# Open the file in read mode
with open("d6.txt", "r") as file:
    # Read all lines from the file
    lines = file.readlines()

# Strip whitespace characters like '\n' and print each line
input_data = [line.strip() for line in lines]



matrix = np.array([list(line) for line in input_data])

rows, cols = matrix.shape
for r in range(rows):
        for c in range(cols):
            if matrix[r][c]=="^":
                rg=r
                cg=c

init_r=rg
init_c=cg

print(matrix[rg][cg])



# Directions dictionary
directions_dict = {
    'U': (-1, 0),  # Up
    'R': (0, 1),   # Right
    'D': (1, 0),   # Down
    'L': (0, -1),  # Left
}

# List of directions in order
order = ['U', 'R', 'D', 'L']

# Function to rotate right
def rotate_right(current_direction='U'):
    current_index = order.index(current_direction)
    new_index = (current_index + 1) % len(order)  # Wrap around using modulo
    new_direction_key = order[new_index]
    return new_direction_key

def get_direction(current_direction='U'):
    return directions_dict[current_direction]

def is_out_of_range(matrix, x, y):
    rows, cols = matrix.shape
    return True if x < 0 or x >= rows or y < 0 or y >= cols else False

cnt = 1
current_direction = 'U'  # Starting direction

test_matrix=deepcopy(matrix)
while True:
    r,c=get_direction(current_direction)
    if is_out_of_range(test_matrix, rg+r, cg+c):
        break
    if test_matrix[rg+r][cg+c]=="#":
        current_direction=rotate_right(current_direction)
    else:
        if test_matrix[rg+r][cg+c]==".":
            test_matrix[rg+r][cg+c]="X"
            cnt+=1
        rg+=r
        cg+=c
#for r in range(rows):
#            print(matrix[r])
print(f"cnt=",cnt)
#part 2
cntloop=0
for a in range(rows):
    for b in range(cols):
        print(a,b,cntloop)
        test_matrix=deepcopy(matrix)
        if not(test_matrix[a][b]=="^" or test_matrix[a][b]=="#"):
            test_matrix[a][b]="#"
        else:
            continue
        rg=init_r
        cg=init_c
        current_direction="U"
    
        
        while True:
            r,c=get_direction(current_direction)
            if is_out_of_range(test_matrix, rg+r, cg+c):
                break
            if test_matrix[rg+r][cg+c]=="#":
                current_direction=rotate_right(current_direction)
            else:
                if test_matrix[rg+r][cg+c]==current_direction:
                    cntloop+=1
                    break
                     
                if test_matrix[rg+r][cg+c] in order :
                    test_matrix[rg+r][cg+c]="+"
                if test_matrix[rg+r][cg+c]==".":
                    test_matrix[rg+r][cg+c]=current_direction
                
                rg+=r
                cg+=c
        

print(f"llopp=",cntloop)

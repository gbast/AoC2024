import numpy as np
import re

# Open the file in read mode
with open("d4.txt", "r") as file:
    # Read all lines from the file
    lines = file.readlines()

# Strip whitespace characters like '\n' and print each line
input_data = [line.strip() for line in lines]


"""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


matrix = np.array([list(line) for line in input_data])

# Dimensions of the matrix
rows, cols = matrix.shape

# The word to search for
word = "XMAS"
word_len = len(word)

# Directions for searching

directions = [
    (0, 1),   # Horizontal right
    (0, -1),  # Horizontal left
    (1, 0),   # Vertical down
    (-1, 0),  # Vertical up
    (1, 1),   # Diagonal down-right
    (-1, -1), # Diagonal up-left
    (1, -1),  # Diagonal down-left
    (-1, 1),  # Diagonal up-right
]

# Function to check if a word exists starting from a given position in a direction
def find_word(matrix, word, start_row, start_col, dir_row, dir_col):
    for i in range(len(word)):
        r = start_row + i * dir_row
        c = start_col + i * dir_col
        if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] != word[i]:
            return False
    return True

# Searching for the word in all directions
count = 0
for row in range(rows):
    for col in range(cols):
        for dir_row, dir_col in directions:
            if find_word(matrix, word, row, col, dir_row, dir_col):
                count += 1

# Output the total count
print(f"The word 'XMAS' appears {count} times in the matrix.")

##part 2
cnt = 0

for r in range(1,rows-1):
    for c in range(1,cols-1):
        if(matrix[r][c]=="A"):
            if (matrix[r-1][c-1]=="M") and (matrix[r-1][c+1]=="M") and (matrix[r+1][c-1]=="S") and (matrix[r+1][c+1]=="S"):
                cnt+=1
            if (matrix[r-1][c-1]=="S") and (matrix[r-1][c+1]=="M") and (matrix[r+1][c-1]=="S") and (matrix[r+1][c+1]=="M"):
                cnt+=1
            if (matrix[r-1][c-1]=="S") and (matrix[r-1][c+1]=="S") and (matrix[r+1][c-1]=="M") and (matrix[r+1][c+1]=="M"):
                cnt+=1
            if (matrix[r-1][c-1]=="M") and (matrix[r-1][c+1]=="S") and (matrix[r+1][c-1]=="M") and (matrix[r+1][c+1]=="S"):
                cnt+=1

print(f"The 'X-MAS' appears {cnt} times in the matrix.")
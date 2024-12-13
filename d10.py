import numpy as np
from queue import Queue

def read_input(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def bfs(matrix, start_r, start_c, rows, cols, directions):
    queue = Queue()
    queue.put((start_r, start_c))
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    reached_nines = set()

    while not queue.empty():
        r, c = queue.get()

        if visited[r][c]:
            continue

        visited[r][c] = True
        current_v = matrix[r][c]


        if current_v == 9:
            reached_nines.add((r, c))
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                if matrix[nr][nc] == current_v + 1:
                    queue.put((nr, nc))
                

    return len(reached_nines)

def all_p(matrix, start_r, start_c, rows, cols, directions): #bfs for sol 2
    queue = Queue()
    queue.put((start_r, start_c))
    cnt = 0

    while not queue.empty():
        r, c = queue.get()

        current_v = matrix[r][c]


        if current_v == 9:
            cnt +=1
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols :
                if matrix[nr][nc] == current_v + 1:
                    queue.put((nr, nc))
                

    return cnt


def main():
    input_data = read_input("d10.txt")
    i_mat = np.array([list(line) for line in input_data])
    rows, cols = i_mat.shape
    matrix = np.array([[int(char) for char in row] for row in i_mat])


    directions = [
        (0, 1),   # right
        (0, -1),  # left
        (1, 0),   # down
        (-1, 0),  # up
    ]

    total_score = 0


    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:  # trailhead 
                total_score += bfs(matrix, r, c, rows, cols, directions)

    print("Sol1: Total paths to 9:", total_score)

    total_score = 0


    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:  #trailhead
                total_score += all_p(matrix, r, c,  rows, cols, directions)

    print("Sol2: Total paths to 9:", total_score)
    
if __name__ == "__main__":
    main()
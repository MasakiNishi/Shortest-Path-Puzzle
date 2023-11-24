import heapq

def solve_puzzle(Board, Source, Destination):
    m, n = len(Board), len(Board[0])
    total_moves = [[float('inf')] * n for _ in range(m)]

    total_moves[0][0] = 0

    min_pq = [(0, 0, 0)] #total_move, row, column
    while min_pq:
        current_total_move, current_row, current_column = heapq.heappop(min_pq)

        if current_row == Destination[0] and current_column == Destination[1]:
            break

        for move_row, move_column in [(-1, 0), (1, 0), (0, -1), (0, 1)]: #up, down, left, right
            new_row, new_column = current_row + move_row, current_column + move_column
            

puzzle = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['#', '-', '#', '#', '-'],
    ['-', '#', '-', '-', '-']
]
print(solve_puzzle(puzzle, (0, 2), (2, 2)))
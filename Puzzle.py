import heapq

def solve_puzzle_helper(Moves, Source, Destination, m, n):
    routes = [Destination]
    total_move = Moves[Destination[0]][Destination[1]]
    current_row, current_column = Destination
    direction = ''

    while total_move>0:
        for key, value in {'D': (-1, 0), 'U': (1, 0), 'R': (0, -1), 'L': (0, 1)}.items():  #down, up, right, left
            new_row, new_column = current_row + value[0], current_column + value[1]
            if 0 <= new_row < m and 0 <= new_column < n: #avoid out of range
                if Moves[new_row][new_column] == total_move - 1: #trace back the routes
                    total_move = Moves[new_row][new_column]
                    routes.append((new_row, new_column))
                    direction = key+direction
                    current_row, current_column = new_row, new_column

    routes.reverse()
    return (routes, direction)

def solve_puzzle(Board, Source, Destination):
    m, n = len(Board), len(Board[0])
    total_moves = [[float('inf')] * n for _ in range(m)]
    total_moves[Source[0]][Source[1]] = 0
    routes = []

    pq = [(0, Source[0], Source[1])] #total_move, row, column
    while pq:
        current_total_move, current_row, current_column = heapq.heappop(pq)

        routes.append((current_row, current_column))

        if (current_row, current_column) == Destination: #when arrive to the destination
            break

        for move_row, move_column in [(-1, 0), (1, 0), (0, -1), (0, 1)]: #up, down, left, right
            new_row, new_column = current_row + move_row, current_column + move_column
            if 0 <= new_row < m and 0 <= new_column < n and Board[new_row][new_column] != '#': #avoid barrier and out of range
                new_total_move = current_total_move + 1

                if new_total_move < total_moves[new_row][new_column]:
                    total_moves[new_row][new_column] = new_total_move
                    heapq.heappush(pq, (new_total_move, new_row, new_column))

    #when can not arrive to the destination
    if total_moves[Destination[0]][Destination[1]] == float('inf'):
        return None

    return solve_puzzle_helper(total_moves, Source, Destination, m, n)

puzzle = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['#', '-', '#', '#', '-'],
    ['-', '#', '-', '-', '-']
]
# print(solve_puzzle(puzzle, (0, 2), (2, 2)))
# print(solve_puzzle(puzzle, (0, 0), (4, 4)))
# print(solve_puzzle(puzzle, (0, 0), (4, 0)))
# print(solve_puzzle(puzzle, (0, 0), (0, 0)))

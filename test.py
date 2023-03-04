board = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]

print(list(map(list, zip(*board[::-1]))))

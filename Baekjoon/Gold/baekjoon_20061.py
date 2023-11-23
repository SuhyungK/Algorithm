# 도노미노도미노 2

def block_one(arr, col):
	row = 0
	while row < 6:
		if arr[row][col] == 1:
			break
		row += 1
	arr[row-1][col] = 1

def block_two(arr, col):
	row = 0
	while row < 6:
		if arr[row][col] == 1 or arr[row][col+1] == 1:
			break
		row += 1
	arr[row-1][col] = 1
	arr[row-1][col+1] = 1

def block_three(arr, col):
	row = 0
	while row < 5:
		if arr[row][col] == 1 or arr[row+1][col] == 1:
			break
		row += 1
	arr[row-1][col] = 1
	arr[row][col] = 1
	
def row_clean(arr):
	global score
	for i in range(5, -1, -1):
		if all(arr[i]):
			arr.pop(i)
			score += 1

def full_arr(arr):
	l = len(arr)
	for _ in range(6 - l):
		arr.insert(0, [0] * 4)

def row_clean2(arr):
	for i in range(2):
		if any(arr[i]):
			arr.pop()

def count_block(arr):
	global total_count
	for row in arr:
		total_count += row.count(1)

func = {
	1: lambda x: block_one(*x),
	2: lambda x: block_two(*x),
	3: lambda x: block_three(*x)
}

N = int(input())
green = [[0] * 4 for _ in range(6)]
blue = [[0] * 4 for _ in range(6)]

score = total_count = 0
for _ in range(N):
	t, x, y = map(int, input().split())
	
	if t == 1:
		func[1]((green, y))
		func[1]((blue, x))
	elif t == 2:
		func[2]((green, y))
		func[3]((blue, x))
	else:
		func[3]((green, y))
		func[2]((blue, x))

	row_clean(green)
	full_arr(green)
	row_clean2(green)
	full_arr(green)

	row_clean(blue)
	full_arr(blue)
	row_clean2(blue)
	full_arr(blue)

count_block(green)
count_block(blue)

print(score)
print(total_count)
print()
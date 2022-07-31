# 리스트 정렬로 중간값 찾기
m = int(input())
num_list = list(map(int,input().split()))
num_list.sort()
print(num_list[m//2])
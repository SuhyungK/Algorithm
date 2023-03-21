# 약수

# 약수 중 가장 큰 수와 작은 수 곱하면 구하려는 수
# 약수의 개수가 홀수여도 위의 방식은 적용됨
# 굳이 홀수라고 가운데 수 제곱할 필요는 없음
N = int(input())
A_list = list(map(int, input().split()))
A_list.sort()
print(max(A_list) * min(A_list))




# 처음 풀이
N = int(input())
A_list = list(map(int, input().split()))
A_list.sort()

if N % 2:
    print(A_list[N // 2] ** 2)
else:
    print(max(A_list) * min(A_list))
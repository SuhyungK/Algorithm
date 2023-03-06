# G4 마약수사대
import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
drugs = {}
for _ in range(M):
    b, f = map(lambda x: ord(x) - 65, input().split())
    if drugs.get(b):
        drugs[b].append(f)
    else:
        drugs[b] = [f]

pub_num, *pub_lst = map(lambda x: ord(x) - 65, input().split())
print(drugs)
drug_pub = drugs.keys() # 마약 공급책 번호를 담은 리스트

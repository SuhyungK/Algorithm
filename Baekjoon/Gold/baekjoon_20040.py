# 사이클 게임

import sys
input = sys.stdin.readline

def main():
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        if (x:=find(x)) < (y:=find(y)):
            parent[y] = x
        else:
            parent[x] = y

    def cycle():
        for t in range(M):
            a, b = map(int, input().split())
            if find(a) == find(b):
                return t+1
            union(a, b)
        return 0

    print(cycle())

N, M = map(int, input().split())
parent = [n for n in range(N)]
main()
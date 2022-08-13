import sys
sys.stdin = open('GNS_test_input.txt')

number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
 
for _ in range(T):
    tc, n = input().split()
    s = list(input().split())
    temp = [0] * 10
     
    for i in range(len(s)):
        temp[number.index(s[i])] += 1
     
    print('%s' %tc)
    for i in range(10):
        print('%s ' %((number[i]+' ')*temp[i]))
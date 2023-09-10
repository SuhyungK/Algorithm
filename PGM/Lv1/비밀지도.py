def convert(num1, num2):
    return bin(num1 | num2)
    
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        row = convert(arr1[i], arr2[i])[2:].zfill(n).replace('1', '#').replace('0', ' ')
        answer.append(row)
    return answer
        
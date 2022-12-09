def binary(n):
    digit = ['1'] + list(bin(n)[2:][::-1]) + ['0']
    idx = digit.index('0')
    digit[idx], digit[idx-1] = '1', '0'
    return int('0b'+''.join(digit[1:][::-1]), 2)
    
def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(binary(num))
        
    return answer
# S1 잃어버린 괄호

string = input() + '+'
nums = []

tmp = ''
is_plus = '+'
for s in string:
    if not s.isdigit():
        nums.append(int(is_plus + tmp))
        tmp = ''
        if s == '-':
            is_plus = '-'
    else:
        tmp += s
print(sum(nums))
# 괄호의 값

bkt = input()
stack = ['']

def check():
    value = {']': 3, ')': 2}
    pair = {']': '[', ')': '('}
    for b in bkt:
        if b in ('(', '['):
            stack.append(b)
            continue

        if type(stack[-1]) != int and stack[-1] != pair[b]:
            return 0

        if type(stack[-1]) == int:
            if stack[-2] != pair[b]:
                return 0
            tmp = stack.pop() * value[b]
            stack.pop()
            stack.append(tmp)
        else:
            stack.pop()
            stack.append(value[b])

        if len(stack) > 3 and type(stack[-1]) == type(stack[-2]) == int:
            tmp = stack.pop() + stack.pop()
            stack.append(tmp)


    if len(stack) > 2 and type(stack[-1]) == type(stack[-2]) == int:
        tmp = stack.pop() + stack.pop()
        stack.append(tmp)

    if len(stack) > 2 or type(stack[-1]) != int:
        return 0
    else:
        return stack[-1]

print(check())
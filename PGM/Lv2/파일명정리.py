def cut(file):
    l = len(file)
    head = '',
    for i in range(l):
        t = file[i]
        if t.isdigit():
            head = file[:i]
            for j in range(i+1, i+5):
                if j < l and not file[j].isdigit():
                    return (head, file[i:j], file[j:])
                elif j >= l:
                    return (head, file[i:], '')
            return (head, file[i:i+5], file[i+5:])
    
def solution(files):
    answer = []
    
    for file in files:
        answer.append(cut(file))
    
    print(answer)
    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))
    
    answer = [''.join(a) for a in answer]
    return answer

print(solution(["img000000", "img1.png","img2","IMG02"]))

#  ["img000012345", "img1.png","img2","IMG02"]
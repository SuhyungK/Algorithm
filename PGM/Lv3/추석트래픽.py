def convert(line):
    _, time, plus = line.split()
    h, m, s = time.split(':')
    end = (int(h)*3600+int(m)*60+float(s))*1000
    start = end-float(plus[:-1])*1000+1
    return start, end
    
def solution(lines):
    def process(start):
        cnt = 0
        for line in lines:
            if start<=line[1] and start+999>=line[0]:
                cnt += 1
        return cnt
    
    lines = list(map(lambda x: convert(x), lines))
    
    answer = 1
    print(lines)
    for line in lines:
        answer = max(answer, process(line[0]), process(line[1]))
    return answer
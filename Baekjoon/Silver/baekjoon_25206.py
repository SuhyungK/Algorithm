# 너의 평점은

subject = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0': 3.0,
          'C+': 2.5, 'C0':2.0, 'D+':1.5, 'D0': 1.0, 'F': 0.0}

t_sum = 0 # 학점의 총합
total = 0 # (학점 * 과목 평점) 의 총합
for _ in range(20):
    a, b, c = input().split()
    
    if c == 'P': continue # 학점이 P라면 지나가기
    t_sum += float(b)
    total += float(b) * subject[c]

print('%.6f' % (total / t_sum))
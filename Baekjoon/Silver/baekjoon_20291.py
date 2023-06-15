# 파일 정리

ext = {}
for _ in range(int(input())):
    _, file = input().split('.')
    ext[file] = ext.get(file, 0)+1

for key in sorted(ext.keys()):
    print(key, ext[key])

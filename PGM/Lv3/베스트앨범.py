def solution(genres, plays):
    N, genre = len(genres), list(set(genres))
    l = len(genre)
    tag = {genre[i]: i for i in range(l)}
    lst = [[j, 0, []] for j in range(l)]
    
    for i in range(N):
        # i : 고유번호, g : genre 태그 번호, p : 재생 횟수
        g, p = tag[genres[i]], plays[i]
        lst[g][1] += p
        lst[g][2].append([plays[i], i])

    lst.sort(key=lambda x: x[1], reverse=1)
    
    ans = []
    for i in range(l):
        lt = lst[i][2]
        lt = list(map(list, zip(*sorted(lt, key=lambda x: (-x[0], x[1])))))
        # print(sorted(lt, key=lambda x: (-x[0], x[1])))
        ans.extend(lt[1][:2])
        
    return ans

print(solution(["classic", "pop", "classic", "classic", "pop"], [800, 600, 150, 800, 2500]))
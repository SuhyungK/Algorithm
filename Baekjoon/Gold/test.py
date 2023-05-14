#  머리 톡톡

def sol():
    def INPUT(lst):
        student = {}
        for i in range(N):
            l = lst[i]
            student[l] = student.get(l, 0) + 1
        return student

    def multiple_judge(student):
        ans = {}
        for num, cnt in student.items():
            ans[num] = ans.get(num, 0) + (cnt-1)
            for j in range(num * 2, 1000001, num):
                if student.get(j):
                    ans[j] = ans.get(j, 0)+student[num]
        return ans
    

    N = int(input())
    lst = list(int(input()) for _ in range(N))

    student = INPUT(lst)
    ans = multiple_judge(student)

    for l in lst:
        print(ans[l])

if __name__ == '__main__':
    sol()
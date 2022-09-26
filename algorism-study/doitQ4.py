import sys
input = sys.stdin.readline
suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
total_num = []
temp = 0

for i in numbers:
    temp = temp + i
    total_num.append(temp)

for i in range(quizNo):
    start, end = map(int, input().split())
    if start == 1:
        print(total_num[end-1])
    else:
        print(total_num[end-1] - total_num[start-2])
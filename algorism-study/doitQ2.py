subnum = int(input())  # 시험을 본 과목의 개수
score = map(int, input().split())
score = list(score)
maxnum = 0
total = 0

for i in score:
    if maxnum <= i:
        maxnum = i

for i in range(len(score)):
    score[i] = score[i] / maxnum * 100

for i in score:
    total = total + i

avgscore = total / len(score)

print(avgscore)
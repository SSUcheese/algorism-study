# 각 학생이 겹치는 경우를 카운트하는 배열을 하나 만들어서 거기서 겹친 횟수를 기록한다
# 예를 들어 1번 학생과 2번 학생이 겹칠 경우,  1번 학생과 2번 학생의 횟수 기록란에 각각 +1
# 입력되는 반 수는 2차원 배열로 받아서 열끼리 비교하는 방식으로 한다
# 마지막으로 횟수 배열에서 가장 큰 학생이 반장이 되는거로 정하고 풀이 종료

num = int(input())
students = []
count = [0] * num  # 각 학생별로 겹친 횟수 기록

for _ in range(num):
    students.append(list(map(int, input().split())))

for i in range(5):
    for j in range(num-1):
        if students[j][i] == students[j+1][i]:
            count[j] += 1
            count[j+1] += 1

answer = count.index(max(count)) + 1

print(answer)

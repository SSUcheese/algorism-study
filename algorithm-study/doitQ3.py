# 이렇게 풀면 시간초과
# 구간 합 공식을 이용해서 접근해야 함
# sys 라이브러리 이용해서 시간초과 피해보자

num1, num2 = input().split()
num1 = int(num1)  # 데이터의 개수
num2 = int(num2)  # 합을 구해야 하는 횟수
numlist = list(map(int, input().split()))

total = []

for i in range(num2):
    sum = 0
    start, end = input().split()
    start = int(start)
    end = int(end)
    for j in range(start - 1, end, 1):
        sum = sum + numlist[j]
    total.append(sum)

for q in total:
    print(q)

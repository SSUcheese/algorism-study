# 숫자의 합 구하기

howmany = int(input())  # 몇개의 숫자가 연달아 입력될 에정인 지 구해 본다
addnum = int(input())  # 실제로 입력될 계산 대상이 될 숫자들

total = 0

for i in range(howmany-1, -1, -1):
    lastnum = (addnum // (10**i))
    total = total + lastnum
    addnum = addnum - (lastnum * (10**i))

print(total)

# 더 깔끔한 풀이

n = input()
numbers = list(input())
sum = 0

for i in numbers:
    sum = sum + int(i)

print(sum)


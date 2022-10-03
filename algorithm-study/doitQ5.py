# 투 포인터 개념으로 접근한다
import sys

def doublepointer(N):
    start_index = 1
    end_index = 1
    count = 1
    while end_index != N:
        sum = 0
        for i in range(start_index, end_index+1, 1):
            sum = sum + i
        if sum < N:
            end_index += 1
        elif sum > N:
            start_index += 1
        else:
            count += 1
            end_index += 1

    return count

input = sys.stdin.readline

num = int(input())

print(doublepointer(num))
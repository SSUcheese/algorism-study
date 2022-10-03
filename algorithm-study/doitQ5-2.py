# 투 포인터로 접근한다
# for문으로 sum 돌리면 시간 초과 뜬다

import sys

def doublepointer(N):
    sum = 1
    start_index = 1
    end_index = 1
    count = 1
    while end_index != N:
        if sum < N:
            end_index += 1
            sum += end_index
        elif sum > N:
            sum -= start_index
            start_index += 1
        else:
            count += 1
            end_index += 1
            sum += end_index

    return count

input = sys.stdin.readline

num = int(input())

print(doublepointer(num))
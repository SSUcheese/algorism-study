import sys

input = sys.stdin.readline

n, m = map(int, input().split())
word = input()
limit = list(map(int, input().split()))

print(word)

record = [0] * 4

start = 0
end = start + m
count = 0

while end < (len(word) + 1):
    print(start)
    start += 1
    for q in range(start, end, 1):
        if word[q] == 'A':
            record[0] += 1
        elif word[q] == 'C':
            record[1] += 1
        elif word[q] == 'G':
            record[2] += 1
        elif word[q] == 'T':
            record[3] += 1
    if (record[0] >= limit[0]) and (record[1] >= limit[1]) and (record[2] >= limit[2]) and (record[3] >= limit[3]):
        count += 1

print(count)


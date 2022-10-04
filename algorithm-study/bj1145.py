num = list(map(int, input().split()))

least = min(num)

while True:
    count = 0
    least += 1
    for q in range(len(num)):
        if least % num[q] == 0:
            count += 1
    if count >= 3:
        print(least)
        break
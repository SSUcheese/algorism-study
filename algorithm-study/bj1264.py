par = True

while par:
    count = 0
    word = input()
    if word == '#':
        break
    for i in range(0, len(word), 1):
        if word[i] in 'aeiouAEIOU':
            count += 1
    print(count)

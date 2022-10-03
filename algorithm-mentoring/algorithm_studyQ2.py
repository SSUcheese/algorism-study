while True:
    try:
        num = int(input())
        tmp = '1'

        while True:
            if int(tmp) % num == 0:
                print(len(tmp))
                break
            tmp += '1'
    except EOFError:
        break
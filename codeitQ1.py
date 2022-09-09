def is_palindrome(word):
    front = 0
    mid = int((len(word) / 2))
    back = int(len(word) - 1)
    count = 0

    for i in range(mid):
        if word[front] == word[back]:
            front += 1
            back -= 1
            count += 1
    if count == mid:
        return True
    else:
        return False


# 코드를 입력하세요.

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
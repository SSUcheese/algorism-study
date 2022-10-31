size = int(input())

candy = [list(map(str, input().rstrip())) for _ in range(size)]


# 답안 체크
def check(arr):
    cnt = 0
    for i in range(size):
        rowStat = 0
        colStat = 0
        rowCnt = 1
        colCnt = 1
        for j in range(size - 1):
            if arr[i][j] == arr[i][j + 1]:
                rowCnt += 1
            else:
                rowStat = max(rowStat, rowCnt)  # 최대 연속 애들 저장
                rowCnt = 1
            if arr[j][i] == arr[j + 1][i]:
                colCnt += 1
            else:
                colStat = max(colStat, colCnt)
                colCnt = 1
        cnt = max(rowStat, colStat, rowCnt, colCnt)

    return cnt



for i in range(size):
    for j in range(size - 1):
        if candy[i][j] != candy[i][j + 1]:
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
            answer = max(answer, check(candy))
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]  # 계산 끝나고 다시 돌려놓기
        if candy[j][i] != candy[j + 1][i]:
            candy[j][i], candy[j + 1][i] = candy[j + 1][i], candy[j][i]
            answer = max(answer, check(candy))
            candy[j][i], candy[j + 1][i] = candy[j + 1][i], candy[j][i]

print(answer)
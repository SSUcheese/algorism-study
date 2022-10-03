# doitQ2보다 더 깔끔한 풀이가 생각나서 다른 방식으로 풀어보았다.
# map 함수의 반환 값은 map 객체이므로 쓰고 나면 꼭 형태 변환을 해줘야만 한다.
# 문제를 풀면서 sum, max와 같은 기본적인 도구들은 적극적으로 활용하자

n = int(input())
mylist = list(map(int, input().split()))
mymax = max(mylist)
sum = sum(mylist)

print(sum * 100 / mymax / n)
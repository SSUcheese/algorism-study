# num1 = int(input())
# num2 = list(map(int, input().split()))
#
# max = num2[0]
# min = num2[0]
#
# for i in range(0, len(num2)):
#     if max < num2[i]:
#         max = num2[i]
#     if min > num2[i]:
#         min = num2[i]
#
# print(max * min)

n = int(input())
nums = list(map(int, input().split()))
print(max(nums) * min(nums))

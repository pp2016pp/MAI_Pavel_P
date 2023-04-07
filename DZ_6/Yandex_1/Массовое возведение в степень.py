n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
p = int(input())

result = []
for num in nums:
    result.append(num**p)
print(result)

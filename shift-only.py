N = int(input())
nums = list(map(int, input().split()))

result = []
for num in nums:
    n = bin(num)
    result.append(len(n) - n.rfind('1') - 1)

print(min(result))

N = int(input())
s = input()

stack = []
for char in s:
    stack.append(char)
    if len(stack) >= 3:
        if stack[-3] == 'f' and stack[-2] == 'o' and stack[-1] == 'x':
            for _ in range(3):
                stack.pop()

print(len(stack))
    

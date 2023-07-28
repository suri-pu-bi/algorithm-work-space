import sys

galho = sys.stdin.readline()

stack = []
top = -1
result = 0
temp = 1

for i in range(len(galho)):
    if galho[i] == '(':
        temp *= 2
        stack.append(galho[i])

    elif galho[i] == '[':
        temp *= 3
        stack.append(galho[i])

    elif galho[i] == ')':
        # stack에 아무것도 없거나 쌍이 맞지 않을경우 0 출력
        if not stack or stack[-1]!='(':
            result = 0
            break
        if galho[i-1] == '(':
            result += temp # 더해주고
        temp //= 2 #
        stack.pop()

    elif galho[i] == ']':
        # stack에 아무것도 없거나 쌍이 맞지 않을경우 0 출력
        if not stack or stack[-1] != '[':
            result = 0
            break
        if galho[i - 1] == '[':
            result += temp  # 더해주고
        temp //= 3  #
        stack.pop()


if stack:
    print(0)

else:
    print(result)
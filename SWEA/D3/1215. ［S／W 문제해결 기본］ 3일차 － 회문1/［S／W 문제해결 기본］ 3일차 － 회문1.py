def solution():
    for i in range(8):
        start = 0
        end = length
        while end != 9:
            code = arr[i][start:end]
            if code == arr[i][-9+end:-9+start:-1]:
                stack.append(code)
            start += 1
            end += 1

    return len(stack)


for test_case in range(1, 11):
    length = int(input())
    arr = [list(input()) for _ in range(8)]
    stack = []
    solution()
    arr = list(map(list, zip(*arr)))
    result = solution()
    print(f'#{test_case} {result}')


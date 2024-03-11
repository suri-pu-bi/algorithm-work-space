import sys
n = int(sys.stdin.readline())
weight = [0]
weight.extend(list(map(int, sys.stdin.readline().split())))
weight.sort()

temp = 0
arr = []
for i in range(len(weight)):
    temp += weight[i]
    arr.append(temp)

flag = False
for i in range(1, len(weight)):
    if arr[i-1] + 1 < weight[i]:
        print(arr[i-1] + 1)
        flag = True
        break

if flag == False:
    print(arr[-1]+1)

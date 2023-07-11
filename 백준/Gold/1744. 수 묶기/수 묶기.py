def find_max_value(valueList):
    value = 0

    if valueList:
        if len(valueList) % 2 != 0:
            for i in range(0, len(valueList) - 1, 2):
                    value += (valueList[i] * valueList[i + 1])
            return value, valueList[-1]

        else:
            for i in range(0, len(valueList), 2):
                    value += (valueList[i] * valueList[i + 1])

            return value, None

    return 0, None


import sys

n = int(sys.stdin.readline())
result = 0
positive = []
negative = []
# 숫자 1은 무조건 더해야 수가 커진다!
for _ in range(n):
    m = int(sys.stdin.readline())

    if m > 1:
        positive.append(m)
    elif m <= 0:
        negative.append(m)
    else:
        result += 1

positive.sort(reverse=True)
negative.sort()


resultNinus, remainNinus = find_max_value(negative)
resultPlus, remainPlus = find_max_value(positive)

if remainPlus != None and remainNinus != None:
    if remainPlus * remainNinus <= remainPlus + remainNinus:
        result += (resultNinus + resultPlus + remainNinus + remainPlus)
    else:
        result += (resultNinus + resultPlus + (remainNinus * remainPlus))

elif remainPlus == None and remainNinus != None:
    result += (resultNinus + resultPlus + remainNinus)

elif remainPlus != None and remainNinus == None:
    result += (resultNinus + resultPlus + remainPlus)

else:
    result += (resultNinus + resultPlus)

print(result)


import sys
n = int(sys.stdin.readline())
words = []
for _ in range(n):
    words.append(list(sys.stdin.readline().rstrip()))

# 가장 자릿수가 높이 있는 알파벳부터 차례대로 9부터 숫자를 부여하는 것을 생각
# -> 예외 발생
# 각 알파벳이 나타난 모든 자릿수를 계산해서 그 값을 토대로 숫자를 부여

# 자릿수를 계산해서 딕셔너리에 넣기 {'A' : 10000}
alpha_value = {}
for word in words:
    for i in range(len(word)):
        if word[i] not in alpha_value:
            alpha_value[word[i]] = 10 ** (len(word) - 1 - i) # 자릿수 표현

        else:
            alpha_value[word[i]] += 10 ** (len(word) -1 - i)

alpha_value = sorted(alpha_value.items(), key=lambda x: x[1], reverse=True)
alpha_to_num = {}

# 알파벳에 숫자 지정하기 {'A' : 9}
num = 9
for alpha in alpha_value:
    alpha_to_num[alpha[0]] = num
    num -= 1

# 단어의 합 구하기
ans = 0
for word in words:
    num = ""
    for i in range(len(word)):
        num += str(alpha_to_num[word[i]])

    ans += int(num)

print(ans)
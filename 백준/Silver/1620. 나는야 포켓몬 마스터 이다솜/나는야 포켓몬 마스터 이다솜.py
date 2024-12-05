'''
처음에는 for문을 돌려 value로 키를 찾는 것을 생각했으나 시간초과 발생

for k, v in mon.items():
    if v == question:
        print(k)

숫자로 주어지면 알파벳을, 알파벳이 주어지면 숫자로 답해야하기 때문에
key값이 int인 dictionary와 key값이 str인 dictionary 두 개를 만들어놓고 찾아야 시간초과가 나지않음
'''

import sys
input = sys.stdin.readline
n,m = map(int, sys.stdin.readline().split())

pokedic_int_key = {}
pokedic_name_key = {}
for i in range(n):
    name = input().rstrip() # 뒤 공백 제거
    pokedic_int_key[i] = name
    pokedic_name_key[name] = i

for _ in range(m):
    question = input().rstrip() # 뒤 공백 제거
    # 입력된 값이 숫자일 경우, key값이 int인 dictionary에서 value를 가져옴
    if question.isdigit():
        print(pokedic_int_key[int(question)-1])
    else:
        print(pokedic_name_key[question]+1)

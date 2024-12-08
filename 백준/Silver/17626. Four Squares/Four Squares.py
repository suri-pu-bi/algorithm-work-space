import sys
n = int(sys.stdin.readline())
# 제곱근 구하기 : i**0.5 또는 math.sqrt
# 계산된 제곱근이 정수인지 확인하기 위해 나머지(소수 부분)를 구함
arr = [0 if i**0.5 % 1 else 1 for i in range(n+1)]
min_value = 4
# 가장 큰 제곱수부터 확인
for i in range(int(n**0.5), 0, -1): # int로 변환시, 소수점은 버리고 정수 부분만 남김
    if arr[n]:
        min_value = 1
        break

    elif arr[n-i**2]: # 나머지가 제곱수일 경우 n = i**2 + (n-i**2)
        min_value = 2
        break

    else:
        for j in range(int((n-i**2)**0.5), 0, -1):
            if arr[(n-i**2)-j**2]: # 제곱수를 한번 더 뺀 나머지가 제곱수일 경우
                min_value = 3

print(min_value)
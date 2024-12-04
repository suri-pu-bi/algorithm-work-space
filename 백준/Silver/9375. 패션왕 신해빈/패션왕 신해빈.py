t = int(input())
for _ in range(t):
  n = int(input())
  wear = {}
  cnt = 1
  for _ in range(n):
    name, kind = input().split()
    if kind in wear.keys():
      wear[kind].append(name)
    else:
      wear[kind] = [name]
    
  cnt = 1
  for i in wear.keys():
    cnt *= (len(wear[i]) + 1) # 해당 종류의 옷을 안입는 경우의 수 포함 
  
  print(cnt-1) # 알몸의 경우의 수인 1 빼주기
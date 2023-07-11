import sys
n = int(sys.stdin.readline())
meeting = []
cnt = 1

for i in range(n):
    startTime, endTime = map(int, sys.stdin.readline().split())
    meeting.append((startTime, endTime))

meeting.sort(key=lambda x: (x[1], x[0]))

minValue = meeting[0][1]
for i in range(1,len(meeting)):
    if minValue <= meeting[i][0]:
        minValue = meeting[i][1]
        cnt += 1

print(cnt)

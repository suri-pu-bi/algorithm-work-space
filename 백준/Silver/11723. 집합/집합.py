
import sys
m = int(sys.stdin.readline())
S = set() # 리스트에 담기에는 메모리 부족

for i in range(m):
    cal_list = list(sys.stdin.readline().split())

    # all이나 empty는 두번째 인자가 주어지지않음
    if len(cal_list) == 1:
        if cal_list[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()

    else:
        num = int(cal_list[1])
        if cal_list[0] == "check":
            print(1 if num in S else 0)

        elif cal_list[0] == "add":
            # set이므로 중복제거 따로 조건처리 안해됨
            S.add(num)

        elif cal_list[0] == "remove":
            if num in S:
                S.discard(num)
            else:
                pass

        elif cal_list[0] == "toggle":
            if num in S:
                S.discard(num)
            else:
                S.add(num)
dict = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

N = int(input())
ok = 1
t = int(10)

CN = int(N)
tt = []
r = 0

while (CN != 0):

    if (N // (t // 10) % 10 != 0):
        r = N % t
        while (r >= 10):
            r = r // 10
        r = r * (t // 10)
        tt.append(r)

    CN = CN // 10
    t = t * 10

rt = ""
for m in tt:
    if m == 0:
        rt = ""
    else:
        if m < 10:
            if m < 4:
                rt = dict[1] * m
            else:
                if m == 4:
                    rt = dict[1] + dict[5]
                else:
                    if m <= 8:
                        rt = dict[5] + dict[1] * (m - 5)
                    else:
                        if m < 10:
                            rt = dict[1] * (10 - m) + dict[10] + rt
        if m >= 10 and m < 100:
            if m < 40:
                rt = dict[10] * (m // 10) + rt
            else:
                if m == 40:
                    rt = dict[10] + dict[50] + rt
                else:
                    if m <= 80:
                        rt = dict[50] + dict[10] * (m // 10 - 5) + rt
                    else:
                        if m < 100:
                            rt = dict[10] * (10 - m // 10) + dict[100] + rt
        if m >= 100 and m < 1000:
            if m < 400:
                rt = dict[100] * (m // 100) + rt
            else:
                if m == 400:
                    rt = dict[100] + dict[500] + rt
                else:
                    if m <= 800:
                        rt = dict[500] + dict[100] * (m // 100 - 5) + rt
                    else:
                        if m < 1000:
                            rt = dict[100] * (10 - m // 100) + dict[1000] + rt
        if m >= 1000:
            rt = dict[1000] * (m // 1000) + rt

print(rt)

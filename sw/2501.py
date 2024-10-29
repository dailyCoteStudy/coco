lst = list(map(int, input().split(" ")))

factor = []
for i in range(1,lst[0]+1):
    if lst[0] % i == 0:
        factor.append(i)

factor = sorted(factor)
if len(factor) >= lst[1]:
    print(factor[lst[1]-1])
else:
    print(0)
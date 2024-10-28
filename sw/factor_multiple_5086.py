# 백준 5086번

while True:
    lst = list(map(int, input().split(" ")))

    if (lst[0] != 0) & (lst[1] != 0):
        if lst[1] % lst[0] == 0:
            print("factor")
        elif lst[0] % lst[1] == 0:
            print("multiple")
        else:
            print("neither")
    else:
         break

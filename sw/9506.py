while True:
    num = int(input())

    if (num > 2) & (num < 100000):
        factor = []
        for i in range(1, num):
            if num % i == 0:
                factor.append(i)

        if sum(factor) == num:
            print(f"{num} = {' + '.join(map(str,factor))}")
        else:
            print(f"{num} is NOT perfect.")
    elif num == -1:
        break  
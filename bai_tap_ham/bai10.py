def daoham(n):
    if n == 0:
        print(1)
    elif n == 1:
        print(2)
    else:
        f0, f1 = 1, 2 
        print(f0)
        print(f1)
        for i in range(2, n + 1):
            fn = 2 * f0 + f1 
            print(fn)
            f0, f1 = f1, fn
n = int(input("Nhập giá trị n: "))
daoham(n)

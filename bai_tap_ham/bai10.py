def daoham(n):
    if n == 0:
        print (1, end=' ')
    elif n == 1:
        print(2, end=' ')
    else:
        f0, f1 = 1, 2 
        print(f0, end=' ')
        print(f1, end=' ')
        for i in range(2, n + 1):
            fn = 2 * f0 + f1 
            print(fn, end=' ')
            f0, f1 = f1, fn
n = int(input("Nhập giá trị n: "))
daoham(n)

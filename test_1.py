n=int(input("Nhập 1 số: "))
for i in range(1,n+1):
    if i*i==n:
        print(n,"là số chính phương")
        break
    elif i**2>n:
        print(n,"không phải là số chính phương")
        break
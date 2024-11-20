n=int(input("Nhập vào số nguyên n"))
i=1
while i<n:
    if i==n:
        print(n,"là số nguyên tố")
        break
    elif n%i==0:
        print(n,"không phải số nguyên tố")
        break 
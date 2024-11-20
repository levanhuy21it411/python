n=int(input("Nhập n: "))
x=0
while n<1 or n>10:
    n=int(input("Nhập n: "))
    while 1<=n<=10 and x<10:
        x+=1
        print(n,"*",x,"=",x*n)
a=float(input("nhập vào a: "))
b=float(input("nhập vào b: "))
c=float(input("nhập vào c: "))
deta=b**2-4*a*c
if a!=0:
    if deta<0:
        print("phương trình vô nghiệm")
    elif deta>0:
        x1=(-b+deta)/(2*a)
        x2=(-b-deta)/(2*a)
        print("phương trình có 2 nghiệm là: x1=",x1,",x2=",x2)
    else:
        print("có nghiệm kép: x1=x2=",(-b/2*a))
else:
    print("phương trình vô nghiệm")                
    

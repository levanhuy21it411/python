d=int(input("Nhập chiều dài: "))
r=int(input("Nhập chiều rộng: "))
def hcn(d,r):
    for i in range(1,r+1):
       print(d*"*")
hcn(d,r)
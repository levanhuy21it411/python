h=int(input("Nhập vào chiều cao"))
space=h
hight=1
for i in range(h):
    if i==0:
        print(space*" "+hight*"*")
    if i < (h-1) :
        hight+=2
        space-=1
        print(space*" "+hight*"*")
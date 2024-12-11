h=int(input("Nhập vào chiều cao"))
def tam_giac_can(h):
    space=h
    hight=1
    for i in range(h):
        if i==0:
            print(space*" "+hight*"X")
        if i < (h-1) :
            hight+=2
            space-=1
            print(space*" "+hight*"X")
tam_giac_can(h)
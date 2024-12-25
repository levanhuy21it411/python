a=int(input("Nhập vào số thập phân: "))
he=int(input("Nhập số hệ muốn đổi: "))
def he_2(a):
    list=[]
    while a>0:
        du=a%2
        list.append(du)
        a=a//2
    for i in range(len(list)-1,-1,-1):
        print(list[i],end=" ")
def he_8(a):
    list=[]
    while a>0:
        du=a%8
        list.append(du)
        a=a//8
    for i in range(len(list)-1,-1,-1):
        print(list[i],end=" ")
def he_16(a):
    list=[]
    while a>0:
        du=a%16
        if du>9:
            if du==10:
                list.append("A")
            if du==11:
                list.append("B")
            if du==12:
                list.append("C")
            if du==13:
                list.append("D")
            if du==14:
                list.append("E")
            if du==15:
                list.append("F")
        else:
            list.append(du)
        a=a//16
    for i in range(len(list)-1,-1,-1):
        print(list[i],end="")
print(f"Chuyển đổi từ hệ {a} sang hệ {he} là :",end=" ")
if he==2:
    he_2(a)
elif he==8:
    he_8(a)
elif he==16:
    he_16(a)
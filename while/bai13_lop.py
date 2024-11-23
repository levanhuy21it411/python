m=int(input("nhập vào độ cao :"))
hight=m
space=0
for i in range (m):
    if i == 0 :
        print("*"*hight)
        hight-=1
    if i < m :
        space+=1
        print("*"*hight + " "*space)
        hight-=1
h=int(input("Nhập chiều cao: "))
space=h-1
high=0
for i in range (h):
    if i == 0 :
        print("*"* high+ " "*space)
    if i <= h :
        space-=1
        high+=1
        print("*"* high + " "*space)
h=int(input("Chiều cao:"))
def tam_giac_nguoc(h):
    for i in range(1,h+1):
        print(h*"X")
        h-=1
tam_giac_nguoc(h)
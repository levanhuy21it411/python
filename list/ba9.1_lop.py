n=int(input("Nhap kích thước danh sách"))

list=[]
def nhap(list,n):
    for i in range(n):
        print("Nhập phần tử thứ",i)
        list.append(int(input()))
    return list
def so_nguyen_to(list,n):
    for i in range(2,n+1):
        for j in range(2,n):
            if i%j==0:
                break
            else:
                print(i)
print(nhap(list,n))

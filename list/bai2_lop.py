n=int(input("Nhap kích thước danh sách"))
list=[]
def nhap(list,n):
    for i in range(n):
        print("Nhập phần tử thứ",i)
        list.append(int(input()))
    return list
def tong(list,n):
    sum=0
    for i in list:
        sum+=i
    print("Tổng các phần tử là:",sum)
print(nhap(list,n))
tong(list,n)
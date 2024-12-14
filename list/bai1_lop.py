n=int(input("Nhap kích thước danh sách"))
list=[]
for i in range(n):
    print("Nhập phần tử thứ",i)
    list.append(int(input()))
print("Xuất mảng vừa mới nhập",list)
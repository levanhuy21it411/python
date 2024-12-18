n=int(input("Nhap kích thước danh sách"))
list=[]
def nhap(list,n):
    for i in range(n):
        print("Nhập phần tử thứ",i)
        list.append(int(input()))
    return list
def tong_le(list,n):
    sum=0
    for i in list:
        if i%2!=0:
            sum+=i
    return sum
print(f"Chương trình có mảng là: {nhap(list,n)}")
print(f"Tổng các số lẻ trong mảng là : {tong_le(list,n)}")            
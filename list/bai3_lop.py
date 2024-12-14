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
    print("Tổng phần tử có giá trị lẻ là",sum)
print(nhap(list,n))
tong_le(list,n)
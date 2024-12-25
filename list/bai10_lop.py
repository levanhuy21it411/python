n = int(input("Nhập kích thước danh sách: "))
list = []
def nhap(list, n):
    for i in range(n):
        print("Nhập phần tử thứ", i + 1)
        list.append(int(input()))
    return list
print(f"Chương trình có mảng là: {nhap(list, n)}")

def kiem_tra_hoan_hao(list, n):
    print("Các số hoàn hảo trong danh sách là:")
    for i in list:
        sum=0
        for j in range(1, i):
            if i % j == 0:
                sum += j
        if sum == i:
            print(f"Số {i} là số hoàn hảo, ở vị trí {vitri(list,i)}")
def vitri(list,number):
    index = 1 
    for i in list:
        if i == number:
            return index
        index += 1
kiem_tra_hoan_hao(list, n)
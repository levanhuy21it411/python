i=1
n=int(input("Nhập vào n"))
dem=0
print("Các số chia hết cho 9 là : ")

while i<n:
    i+=1
    if i%9==0:
        dem+=1
        print(i)
print("Số in ra màn hình là: ", dem)  
    
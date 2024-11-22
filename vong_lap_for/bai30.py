a =int(input("Nhập số a: "))
dem=0
for i in range(1,a+1):
    if a%i==0:
        dem=dem+1
print("Đếm số ước của a là: ",dem)
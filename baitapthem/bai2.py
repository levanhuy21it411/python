a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
ucln=0
if a==0 and b==0:
    ucln='không xác định(bất kỳ số nguyên dương nào cũng là ước của 0)'
    bcnn='không xác định'
elif a==0 or b==0:
    if a>b:
        for i in range(1,a+1):
            if a%i==0 and b%i==0:
                ucln=i
    else:
        for i in range(1,b+1):
            if a%i==0 and b%i==0:
                ucln=i
    bcnn='không xác định'
else:
    if a>b:
        for i in range(1,a+1):
            if a%i==0 and b%i==0:
                ucln=i
    else:
        for i in range(1,b+1):
            if a%i==0 and b%i==0:
                ucln=i
    bcnn= abs(a * b) // ucln
print('ước chung lỡn nhất là',ucln)
print('bội chung nhỏ nhất là',bcnn)
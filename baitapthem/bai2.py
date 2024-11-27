a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
ucln=0
a_goc = a
b_goc = b
for i in range(1,a+1):
   if a%i ==0 and b%i==0:
       ucln=i
bcnn = (a_goc * b_goc) // ucln
print("Ước chung lớn nhất của hai số là:", ucln)
print("Bội chung nhỏ nhất của hai số là:", bcnn)

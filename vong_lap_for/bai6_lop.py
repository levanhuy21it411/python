n=int(input("Nhập bảng cửu chương : "))
if 1<=n<=10:
 for i in range (1,11):
    print(i,"*",n,"=",i*n)

else:
    print("lỗi nhập lại")
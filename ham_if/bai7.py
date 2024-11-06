a=int(input("nhập vào số năm: "))
if (a%4==0 and a%100!=4) or a%400==0:
    print("là năm nhuận")
else:
    print("là năm không nhuận")
s=int(input("Nhập vào số giây: "))
h=s//(60*60)
p=(s%(60*60))//60
s=s%60
print(h,"giờ",p,"phút",s,"giây")  


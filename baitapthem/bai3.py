x = int(input("Nhập x: "))
n = int(input("Nhập n: "))
tam=x
if n==0:
    x=1 
else:
  for i in range(1,n):
    x=x*tam
print(tam,"^",n,"=",x)

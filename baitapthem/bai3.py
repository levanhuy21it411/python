x = int(input("Nhập x: "))
n = int(input("Nhập n: "))
tam=x
for i in range(1,n):
    x=x*tam
print(tam,"^",n,"= ",x)

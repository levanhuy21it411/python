n=int(input("nhập vào n: "))
dem=0
for i in range(1,n+1):
    if i%5==0:
      dem+=1
print(dem)
n=int(input("Nhập một số ( n>0) "))
print("Các số lẻ từ 1 đến",n,"là:",end='\t')
for i in range(1,n+1):
    if i%2!=0:
       print(i,end=' ')

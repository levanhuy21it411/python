
n=int(input("nhập một số nguyên: "))

for i in range(2,n):
    if i==n:

       print(n,"là số nguyên tố")
       break
    elif n%i==0:
           print(n,"không phải số nguyên tố")
           break 
      
       
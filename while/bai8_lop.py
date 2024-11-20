n=int(input("Nhập vào số nguyên n"))
i=1
while i<n:
    if (n%i==0) and (n//i==n):
        print(n,"là số nguyên tố")
        break 
    else:
      print(n,"Không phải là số nguyên tố")
      break
       
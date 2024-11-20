n=int(input("nhập số n : "))
sum=0
while n!=0:
    a=n%10 
    n=n//10
    sum+=a
print(sum)
n=int(input("NHập một số n"))
i=1
sum=0
while i<n:
    if n%i==0:
        sum+=i
    i+=1

if sum==n:
    print("là số hoàn hảo")
else:
    print("không phải là số hoàn hảo")
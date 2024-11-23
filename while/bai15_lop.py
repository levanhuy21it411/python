n=int(input("Nhập số n: "))
i=0
s1=1
s2=0
while i<n+1:
   if s1+s2<n:
       s=s1+s2
       print(s,end=" ")
       s1=s2
       s2=s
       
       
        
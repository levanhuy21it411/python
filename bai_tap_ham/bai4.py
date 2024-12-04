n=int(input("Nhập số n: "))
def fibonaxi(n):
    i=0
    s1=1
    s2=0
    while i<n:
        if s1+s2<n:
            s=s1+s2
            print(s,end=" ")
            s1=s2
            s2=s
print("Dãy số fibonaxi là:",fibonaxi(n))
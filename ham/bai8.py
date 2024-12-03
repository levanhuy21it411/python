n=int(input("nhập một số nguyên"))
def mang(n):
 for i in range(1,n+1,2):
    print (i,end="\t")
    if i%10==9:
        print()
print(mang(n))
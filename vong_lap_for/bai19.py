n=int(input("nhập một số nguyên"))
for i in range(1,n+1,2):
    print (i,end=" ")
    if i%10==9:
        print()
# if i % 9!=0:
#     print() 
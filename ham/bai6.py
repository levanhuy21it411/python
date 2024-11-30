n=int(input("Nhập n: "))
def chanle(n):
    if n%2==0:
        a="chẵn"
    else:
        a="lẻ"
    return a
print("số n là số : ",chanle(n))
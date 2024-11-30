n=int(input("Nhập n: "))
def chanle(n):
    if n%2==0:
        return str("Chẵn")
    else:
        return str("Lẻ")
print("số n là số : ",chanle(n))
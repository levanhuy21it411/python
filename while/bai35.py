# Nhập n từ người dùng
n = int(input("Nhập n: "))

k = 0
S_k = 0

while S_k<n:
    k =k+1
    S_k =S_k+k
    if S_k >= n:
        k =k-1
        break

print("Giá trị k lớn nhất sao cho S(k) nhỏ hơn n là:", k)

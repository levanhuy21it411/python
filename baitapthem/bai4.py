n = int(input("Nhập một số nguyên: "))
tich_chan = 1
tong_le = 0
while n > 0:
    a = n % 10
    n //= 10
    if a % 2 == 0: 
        tich_chan *= a
    else: 
        tong_le += a
print("Tích các chữ số chẵn:", tich_chan)
print("Tổng các chữ số lẻ:",tong_le)

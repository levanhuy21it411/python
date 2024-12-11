n=int(input("Nhập n: "))
def so_nguyen_to(n):
  for i in range(2, n + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=" ")
so_nguyen_to(n)
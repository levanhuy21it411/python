def kiem_tra_nguyen_to(so):
    if so <= 1:
        return 0
    for i in range(2, int(so**0.5) + 1):
        if so % i == 0:
            return 0
    return 1
def nhap_danh_sach(so_phan_tu):
    danh_sach = []
    print(f"Nhập {so_phan_tu} phần tử cho danh sách:")
    for i in range(so_phan_tu):
        gia_tri = int(input(f"Nhập phần tử thứ {i + 1}: "))
        danh_sach.append(gia_tri)
    return danh_sach
def tim_so_nguyen_to(danh_sach):
    so_nguyen_to = []
    for so in danh_sach:
        if kiem_tra_nguyen_to(so) == 1:
            so_nguyen_to.append(so)  
    if so_nguyen_to:
        print("Các số nguyên tố trong danh sách là:", so_nguyen_to)
    else:
        print("Không có số nguyên tố nào trong danh sách.")
kich_thuoc = int(input("Nhập kích thước của danh sách: "))
danh_sach = nhap_danh_sach(kich_thuoc)
print("Danh sách vừa nhập là:", danh_sach)
tim_so_nguyen_to(danh_sach)


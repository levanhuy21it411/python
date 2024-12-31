
so_phim = [2, 3, 4, 5, 6, 7, 8, 9]
chu_cai = [
    "ABC",    
    "DEF",
    "GHI",
    "JKL",    
    "MNO",   
    "PQRS",   
    "TUV",  
    "WXYZ"    
]

mat_thu=int(input("Nhập mật thư"))
mat_thu
ket_qua = ""
for ky_tu_ma_hoa in mat_thu.split():
    so_phim_nhap = int(ky_tu_ma_hoa[0])
    so_lan = len(ky_tu_ma_hoa)          
    if so_phim_nhap in so_phim:
        index = so_phim.index(so_phim_nhap) 
        chuoi_chu_cai = chu_cai[index]     
        chi_so = (so_lan - 1) % len(chuoi_chu_cai)
        chu_giai_ma = chuoi_chu_cai[chi_so]
        ket_qua += chu_giai_ma

print("Kết quả giải mã:", ket_qua)

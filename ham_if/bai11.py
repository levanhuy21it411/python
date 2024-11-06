# Nhập năm dương lịch
sonam = int(input("Nhập năm dương lịch: "))

# Tìm Thiên Can
can=sonam % 10
if can == 0:
    can = "Canh"
elif can == 1:
    can = "Tân"
elif can == 2:
    can = "Nhâm"
elif can == 3:
    can = "Quý"
elif can == 4:
    can = "Giáp"
elif can == 5:
    can = "Ất"
elif can == 6:
    can = "Bính"    
elif can == 7:
    can = "Đinh"
elif can == 8:
    can = "Mậu"
elif can == 9:
    can = "Kỷ"
# Tìm Địa Chi
chi = sonam % 12
if chi == 0:
    chi = "Thân"
elif chi == 1:
    chi = "Dậu"
elif chi == 2:
    chi = "Tuất"
elif chi == 3:
    chi = "Hợi"
elif chi == 4:
    chi = "Tý"
elif chi == 5:
    chi = "Sửu"
elif chi == 6:
    chi = "Dần"
elif chi == 7:
    chi = "Mão"
elif chi == 8:
    chi = "Thìn"
elif chi == 9:
    chi = "Tỵ"
elif chi == 10:
    chi = "Ngọ"
elif chi == 11:
    chi = "Mùi"

# Ghép Thiên Can và Địa Chi để tạo ra năm âm lịch
licham = can + " " + chi

# In kết quả
print("Năm âm lịch:", licham)

sonam=int(input("số năm:"))
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
#thiencan
if can==("Giáp") or can==("Ất"):
    can=1
elif can==("Bính") or can==("Đinh"):
    can=2
elif can==("Mậu") or can==("Kỷ"):
    can=3
elif can==("Canh") or can==("Tân"):
    can=4
elif can==("Nhâm") or can==("Quý"):
    can=5
#Địa chi
if chi==("Tý") or chi==("Sửu") or chi==("Ngọ") or chi==("Mùi"):
    chi=0
elif chi==("Dần") or chi==("Mão") or chi==("Thân") or chi==("Dậu"):
    chi=1
elif chi==("Thìn") or chi==("Tuất") or chi==("Tỵ") or chi==("Hợi"):
    chi=2
menh=can+chi
if menh>5:
      menh=menh-5
if menh==1:
    print("mệnh Kim")
elif menh==2:
    print("mệnh Thủy")
elif menh==3:
    print("mệnh Hỏa")
elif menh==4:
    print("mệnh Thổ")
elif menh==5:
    print("mệnh Mộc")     
str=input("Nhập một sâu chuỗi :")
kiemtra=input("Nhập một chữ cần tìm :")
if kiemtra in str:
    print(f"{kiemtra} có tìm thấy trong chuỗi {str}")
else:
    print(f"{kiemtra} không tìm thấy trong chuỗi {str}")
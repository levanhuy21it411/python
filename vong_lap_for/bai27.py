h=int(input("nhập độ cao h : "))
space_1=h-1
space_2=1
for i in range(h):
   if i==0:
    print(space_1*" "+"*")
   elif i<h-1:
      space_1=space_1-1
      print(space_1*" "+"*"+space_2*" "+"*")
      space_2=space_2+2
else:
   print(((h*2)-1)*"*")
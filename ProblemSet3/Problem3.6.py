pattern = ""

for beat in range (16):
    if beat==0 :
        pattern += "B   "
    elif beat % 4 ==3 :
        pattern += "t   "
    elif beat % 4 ==2:
        pattern +="K   "
    elif beat== 1:
        pattern += "t   "
    elif beat% 4 == 0:
        pattern += "t   "
    elif beat % 4 ==1:
        pattern += "b   "

print(pattern)
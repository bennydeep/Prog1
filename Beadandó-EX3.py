def inframe(text):
    str=''
    szavak=[]
    for i in text:
        if i==' ':
            szavak.append(str)
            str=''
        else:
            str+=i
    szavak.append(str)




text=input("Írj be valamit")
print(inframe(text))
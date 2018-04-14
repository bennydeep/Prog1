text=input("Írj be valamit")

szo=''
szavak=[]
for i in text:
    if i==' ':
        szavak.append(szo)
        szo=''
    else:
        szo+=i
szavak.append(szo)


print(szavak)

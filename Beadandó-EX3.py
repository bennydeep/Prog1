szoveg=input("Írj be valamit")

szo=''
szavak=[]
for i in szoveg:
    if i==' ':
        szavak.append(szo)
        szo=''
    else:
        szo+=i
szavak.append(szo)

leg_h=0
for i in szavak:
    if len(i)>leg_h:
        leg_h=len(i)

csillag_csillag='' #díszítősor :D
for i in range(leg_h+5):
    csillag_csillag+='&'

print(csillag_csillag)
for i in szavak:
    space=leg_h-len(i)
    print('&',i,' '*space,'&')
print(csillag_csillag)
#print(szavak)

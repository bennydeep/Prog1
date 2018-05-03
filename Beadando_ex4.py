import string

def clearrow(str):
    newstr=""
    for ch in str:
        if ch not in string.punctuation and ch!='\n':
            newstr+=ch
    return newstr.lower()




szoveg=str(input("Írj be valamit"))
#print(clearrow(szoveg))
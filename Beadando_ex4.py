import string

def malackodas(str):
    words=newstr.split(' ')
    #return words
    for word in words:
        print(word[1:] + word[0] + "ay", end=" ")



szoveg=str(input("Írj be valamit"))
newstr=""
for ch in szoveg:
    if ch not in string.punctuation and ch!='\n':
        newstr+=ch
newstr=newstr.lower()


malackodas(str)

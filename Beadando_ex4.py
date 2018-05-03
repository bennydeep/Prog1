import string

def malackodas(str):
    words=newstr.split(' ')
    #return words
    for word in words:
        if word=="ay":
            return -1
        elif word[-2:]=="ay":
            x=word[0:len(word)-2]
            return(x[-1]+x[0:len(x)-1]+' ').capitalize()
        else:
            return(word[1:] + word[0] + "ay"+' ').capitalize()

mondat=str(input("Írj be valamit"))
newstr=""
for ch in mondat:
    if ch not in string.punctuation and ch!='\n':
        newstr+=ch
newstr=newstr.lower()


print(malackodas(str))

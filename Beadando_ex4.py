import string

def malackodas(str):
    words=newstr.split(' ')
    #return words
    for word in words:
        if word[-3:]=="ay":
            word=word[0:len(word)-2]
            print(word[-1]+word,end=" ")

        else:
            print(word[1:] + word[0] + "ay", end=" ")

mondat=str(input("Írj be valamit"))
newstr=""
for ch in mondat:
    if ch not in string.punctuation and ch!='\n':
        newstr+=ch
newstr=newstr.lower()


(malackodas(str))

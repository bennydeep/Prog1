n=0
while True:
    try:
        n=int(input("adjon meg egy szamot: "))
        break
    except ValueError:
        print("nem megfelelo szamformatum")
print(n,type(n))
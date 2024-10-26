def harmas():
    szam = int(input("Adj meg egy szamot"))
    if szam > 49 and szam < 901 and szam % 11 !=0:
        for i in range(50,901,1):
            print(f"|{i}",end="|")


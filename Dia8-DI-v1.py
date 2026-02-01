numP = [0,2,4,6,8]
numImp = [1,3,5,7,9]

def VIP(num):
    Fnum = num % 10
    if Fnum in numP:
        print("Número par")
    elif Fnum in numImp:
        print("Número impar")
    else:
        print("Informe um número")


Num = input("Informe o número: ")
NumInt = int(Num)
VIP(NumInt)
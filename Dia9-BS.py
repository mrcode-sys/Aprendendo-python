num1=int(input("Informe um número: 1"))
num2=int(input("Informe outro número: "))
def numMaiMen(a, b):
    if a < b:
        return b, a
    elif a == b:
        return "Os valores são iguais"
    else:
        return a, b

if len(numMaiMen(num1, num2)) != 2:
    print(numMaiMen(num1, num2))
else:
    NumMai, NumMen = numMaiMen(num1, num2)
    print("O maior valor é",NumMai,"e o menor valor é",NumMen)
idade1=1
idade2=5
def calcIdade():
    idade1=2
    idade2=7
    idade3=3
    idade4=4
    print(idade1) #resultado: 2
    print(idade2) #resultado: 7
    print(idade3) #resultado: 4
    calc= idade1 - idade2
    difIdade=abs(calc)
    print(difIdade) #resultado:5
    return idade4
calcIdade()

print(idade1) #resultado: 1
print(idade2) #resultado: 5
print(calcIdade()) #resultado: 4
# print(idade3) #resultado: erro
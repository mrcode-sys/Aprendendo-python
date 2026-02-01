# variaveis
repetições = 0
IncorrectName = True
names = ["marcos","Marcos","Camila","camila"]
dinheiroAnt = float("1000.11")
dinheiroDps = float("4.00")
dinheiro = dinheiroAnt - dinheiroDps
dinheiroTotal = round(dinheiro, 2)

while IncorrectName == True:
    name = input("Insira seu nome: ")
    if name in names:
        IncorrectName = False

        if dinheiroDps > 20.00:
            print("Você é", name, "e gastou ",dinheiroTotal, "reais")

        elif dinheiroDps <= 20.00 and dinheiroDps >= 5.00:
            print("Você é", name, "e ficou pobre")
        elif dinheiroDps < 5.00:
            print("seu pobre")
            repetições = repetições + 1
            print (repetições)
    else:
        print("...")
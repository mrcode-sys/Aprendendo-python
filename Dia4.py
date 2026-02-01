iniciar = False
comandoIniciar = input('iniciar com "s"')
if comandoIniciar == "s":
    print("Qual seu nome?")
    name = input()

    erro = True
    while erro == True:
        print("Qual a sua idade?")
        idade = input()
        try:
            idade1 = int(idade)
            erro = False
        except:
            print(f'escreva um número, não "{idade}"')
    if idade1 <= 1000:
        print(f"Você é {name} e tem {idade1} anos")

        if idade1 < 18:
            print("Você é menor de idade")
        elif idade1 >= 18 and idade1 <= 200:
            print("Você é maior de idade")
        elif idade1 > 200:
            print("Você é uma múmia")
fechar=False

while fechar==False:
    palavra=input("Informe uma palavra frase ou número, q para sair:")
    if palavra == "q":
        fechar=True
    else:
        for letra in palavra:
            print(letra)
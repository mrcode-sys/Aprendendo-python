erros = True
dias = {1: "Domingo", 2:"Segunda", 3:"Terça", 4:"Quarta", 5:"Quinta", 6:"Sexta", 7:"Sábado"}
while erros == True:
    try:
        numero1 = input("informe um número de 1 à 7 para dias da semana, q para sair:")
        if numero1.lower() == "q":
            erros = False
        else:
            numeroInt = int(numero1)
            dia=dias.get(numeroInt)

            if dia:
                print(dia)
            else:
                print("Nunca vi uma semana de", numeroInt, "dias")
    except:
        print("Informe um caractere válido")
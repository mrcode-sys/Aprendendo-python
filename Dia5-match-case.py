erros = True

while erros == True:
    try:
        numero1 = input("informe um número de 1 à 7 para dias da semana, q para sair:")
        if numero1 == "q":
            erros = False
        else:
            numero = int(numero1)
            match numero:
                case 1:
                    print("Domingo")
                case 2:
                    print("Segunda")
                case 3:
                    print("Terça")
                case 4:
                    print("Quarta")
                case 5:
                    print("Quinta")
                case 6:
                    print("Sexta")
                case 7:
                    print("Sábado")
                case _:
                    print("Nunca vi uma semana de", numero, "dias")
    except:
        print("Informe um caractere válido")        
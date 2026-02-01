erros = True

while erros == True:
    try:
        numero1 = input("informe um número de 1 à 7 para dias da semana, q para sair:")
        if numero1 == "q":
            erros = False
        else:
            numero =int(numero1)
            if numero != 0 and numero <= 7:
                if numero == 1:
                    print("Domingo")
                if numero == 2:
                    print("Segunda")
                if numero == 3:
                    print("Terça")
                if numero == 4:
                    print("Quarta")
                if numero == 5:
                    print("Quinta")
                if numero == 6:
                    print("Sexta")
                if numero == 7:
                    print("Sábado")
            else:
                print("Nunca vi uma semana de", numero, "dias")
    except:
        print("Informe um caractere válido")        
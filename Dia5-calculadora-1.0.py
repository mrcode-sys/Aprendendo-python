Fechar=False
calc = "#"
while Fechar==False:
    ErroInt1=True
    ErroInt2=True
    ErroCalc=True
    while ErroInt1==True:
        try:
            num1str=input("informe um número, q para sair:")
            if num1str=="q":
                ErroInt1=False
                ErroInt2=False
                ErroCalc=False
                Fechar=True
            else:
                num1=int(num1str)
                ErroInt1=False
        except:
            try:
                num1=float(num1str)
                ErroInt1=False
            except:
                print("Informe um número válido, não", num1str)

    while ErroCalc==True:
        calc=input("informe um cálculo:")
        if calc == "+" or calc == "-" or calc == "/" or calc == "*" or calc == "%":
            ErroCalc=False
        else:
            print("Informe um número válido, não", calc)

    while ErroInt2==True:
        try:
            num2str=input("informe um número:")
            num2=int(num2str)
            ErroInt2=False
        except:
            try:
                num2=float(num2str)
                ErroInt2=False
            except:
                print("Informe um número válido, não", num2str)
    if calc == "+" or calc == "-" or calc == "*" or calc == "/" or calc == "%":
        match calc:
            case "+":
                print(num1+num2)
            case "-":
                print(num1-num2)
            case "*":
                print(num1*num2)
            case "/":
                if calc != 0:
                    res=str(num1/num2)
                    resInt=res.split(".")
                    if resInt[1] != "0":
                        print(res)
                    else:
                        print(resInt[0])
            case "%":
                print(num1%num2)

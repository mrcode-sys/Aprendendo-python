ErroCalc=True
Fechar=False
calc = "#"

while Fechar==False:
    while ErroCalc==True:
        try:
            calcStr=input("informe um número uma fórmula e outro número, q para sair:")
            if calcStr=="q":
                ErroCalc=False
                Fechar=True
            else:
                calc=calcStr.split()
                try:
                    form=calc[1]
                    num1Str=calc[0]
                    num2Str=calc[2]
                except:
                    print("Informe uma fórmula válida, não", calc)
                    break
                try:
                    num1=int(num1Str)
                    num2=int(num2Str)
                except:
                    try:
                        num1=float(num1Str)
                        num2=float(num2Str)
                    except:
                        print("Informe uma fórmula válida, não", calc)
                        break 
                ErroICalc=False
                match form:
                    case "+":
                        print(num1+num2)
                    case "-":
                        print(num1-num2)
                    case "*":
                        print(num1*num2)
                    case "/":
                        if num1 != 0 and num2 != 0:
                            calcDivis=str(num1/num2)
                            calcDivisInt=calcDivis.split(".")
                            if calcDivisInt[1] != "0":
                                print(calcDivis)
                            else:
                                print(calcDivisInt[0])
                        else:
                            print("Informe um número diferente de zero")
                    case "%":
                        print(num1%num2)
                    case _:
                        print("Informe uma fórmula válida, não", form)
                        print(form)
                        break
        except:
            print("Informe um cálculo válido, não", calcStr)
            break
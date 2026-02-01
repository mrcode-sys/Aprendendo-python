import time
import random

erroCalc=True
fechar=False
calc = "#"
formulas=["-","+","/","*","%"]
formula=""
Num1=""
Num2=""

while fechar==False:
    Num1=""
    Num2=""

    calcStr=input("informe um número uma fórmula e outro número, q para sair:")

    if calcStr=="q":
        numAleat=random.randint(1, 20)
        time.sleep(0.4)
        print("fechando.")
        time.sleep(0.20)
        print("fechando..")
        if numAleat >= 3:
            time.sleep(0.20)
            print("fechando...")
        if numAleat >= 5:
            time.sleep(0.20)
            print("fechando.")
        if numAleat >= 7:
            time.sleep(0.20)
            print("fechando..")
        if numAleat >= 11:
            time.sleep(0.20)
            print("fechando...")
        if numAleat >= 14:
            time.sleep(0.20)
            print("fechando.")
        if numAleat >= 17:
            time.sleep(0.20)
            print("fechando..")
        if numAleat == 20:
            time.sleep(0.20)
            print("fechando...")
            time.sleep(0.21)
        fechar=True
    else:
        for calcStrSep in calcStr:
            if calcStrSep in formulas:
                formula=calcStrSep

        for num1 in calcStr:
            if num1 in formulas:
                break
            else:
                Num1+=num1

        for num2 in calcStr:
            if num2 in formulas:
                Num2=""
            else:
                Num2+=num2
        try:
            Num1Int=int(Num1)
            Num2Int=int(Num2)

            match formula:
                case "+":
                    print(Num1Int+Num2Int)
                case "-":
                    print(Num1Int-Num2Int)
                case "*":
                    print(Num1Int*Num2Int)
                case "/":
                    if Num1 != "0" and Num2 != "0":
                        print(Num1Int/Num2Int)
                    else:
                        print("Informe um número diferente de zero")
                case "%":
                    print(Num1Int%Num2Int)
                case _:
                    print("Digite um cálculo válido, não",formula)

        except:
            print("Informe um cálculo válido, não",calcStr)
numc = False
num1 = input("Informe um número: ")
if num1 != "0":
    while numc == False:
        num2 = input("Informe outro número: ")
        if num2 == "0":
            print("Foi digitado o número 0")
            numc = True
else:
    print("Foi digitado o número 0")
    numc = True0
import random
numc = False
cat1 = ["n","nao","não","no","nunca","never","hoje não"]
cat2 = ["y","s","sim","yes","yep","yup","yeah"]
a=random.randint(1, 20)

while numc == False:
    num = input("advinhe o número de 1 a 20: ")
    try:
        numInt = int(num)
    except:
        print("informe um número")
    if numInt < a:
        print("maior")
    if numInt > a:
        print("menor")
    if numInt == a:
        print("certo")
        cont = input("continuar?")
        if cont.lower() in cat1:
            break
        elif cont.lower() in cat2:
            a=random.randint(1, 20)
            continue
        else:
            print("informe y/s ou n")
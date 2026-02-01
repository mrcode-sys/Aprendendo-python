import time
import random

fechar=False

while fechar==False:
    calcStr=input("informe uma fórmula, q para sair:")

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
        try:
            result = eval(calcStr)
            print(result)
        except:
            print("Informe um cálculo válido, não",calcStr)
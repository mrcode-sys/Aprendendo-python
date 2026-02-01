import json

dic = {}
result = {}

eleitos = ["lula", "bolsonaro"]
print("Programação Urna")

cont = True

while cont == True:
    nome = input("Nome:> ").lower()
    voto = input("Voto:> ").lower()
    if nome.lower() in dic:
        print("Usuário já votou")

    else:
        if voto in eleitos:
            dic[nome] = voto
            print(nome.title()+" Votou em "+voto.title())
        else:
            print("Eleito não candidato")

    resp = input("Novo voto? ").lower()
    if resp == "sim":
        cont = True
    
    else:
        cont = False
resp = input("Apurar votos? ")
if resp.lower() == "sim":
    for user in dic:
        voto = dic[user]
        
        if voto not in result:
            result[voto] = 0
        result[voto] = result[voto] + 1
    print(result)

    totalVotos = 0

    for num in result.values():
        totalVotos = totalVotos + num
    
    for eleito in result:
        votoEleito = result[eleito]
        porc = votoEleito / totalVotos * 100

        print(eleito+": ",porc)
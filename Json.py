import json
nomes = []

try:
    lista = open('Nomes.json','r')
except FileNotFoundError:
    print("Json inexistente, criando novo")
    lista = open('Nomes.json', 'w')
    result = lista.write('[]')
    lista.close()
    lista = open('Nomes.json','r')
    print(result)
nomes = json.load(lista)

print('Nomes na lista: ', nomes)

lista.close()
print("Fazer inscrição?")
resp = input(":> ")
resp = resp.lower()
print(resp)
if resp == "sim":
    print("Nome:")
    resp = input(":> ")

    nomes.append(resp)
    lista = open('Nomes.json','w')
    json.dump(nomes, lista)
    lista.close
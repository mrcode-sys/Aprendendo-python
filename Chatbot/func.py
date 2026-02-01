import sys
import subprocess as s
import os
import json
import difflib

def sistema(programa):
    sistema = sys.platform
    if 'win' in sistema:
        os.startfile(programa)
    if 'linux' in sistema:
        try:
            s.Popen(programa)

        except FileNotFoundError:
            try:
                s.Popen(['xdg-open',programa])

            except FileNotFoundError:
                print("Programa não encontrado")

def openJson(arq):
    try:
        lista = open(arq,'r')
    except FileNotFoundError:
        print("Json inexistente, criando novo")
        lista = open(arq, 'w')
        result = lista.write('{}')
        lista.close()
        lista = open(arq,'r')
        print(result)

    return json.load(lista)
    lista.close()

def savJson(arq, escrever):
    lista = open(arq,'w')
    json.dump(escrever, lista)
    lista.close
def compResp(resp):
    sysPalavras = ['executar','aprende','oi','olá',"Alt F4"]
    palavras = openJson('frDic.json')

    correcao = difflib.get_close_matches(resp,sysPalavras,n=1,cutoff=0.5)
    if correcao:
        if 'executar' in correcao:
            program = resp.split()[-1]
            correcao = correcao[0]+' '+program
            return correcao
        else:
            return correcao[0]
    else:
        correcao = difflib.get_close_matches(resp,palavras,n=1,cutoff=0.7)
        if correcao:
            return correcao[0]
        else:
            return resp
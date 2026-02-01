nome = "Lucas"
idade = 10
esta_chovendo = True
chuva = ""
if esta_chovendo == False:
    chuva = "não está chovendo,"
elif esta_chovendo == True:
    chuva = "está chovendo,"

print(f"seu nome é {nome} e tem {idade} anos. {chuva} Logo está chovendo é {esta_chovendo}. {nome} é uma {type(nome)}, {idade} é uma {type(idade)}, {esta_chovendo} é uma {type(esta_chovendo)}, {chuva} é uma {type(chuva)}.")
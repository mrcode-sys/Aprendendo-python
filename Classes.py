class classe():

    print('Rodando classe')

    def __init__(self, a): # Roda ao rodar a classe
        print('Rodando Init')
        print(a) # printa valor definido na linha 13 após rodar a classe
        self.Nome = a # adiciona um atributo ao self, self é como se fosse o que rodou, o atributo é definido em A que é o que rodou, na linha 13

    def Teste(self): # função que é executada na linha 14
        print('Teste1')

a = classe('Teste') # executa a classe e envia valor
b = a.Teste() # Roda função dentro da classe
print(a.Nome) # Printa Atributo Nome definido dentro da classe
import func
class brain:

    def __init__(self):
        self.resplist = ['oi', 'olá']
        self.botHistorico = []
        self.nameUser = None
        self.acaod = {}
        self.acaod = func.openJson('frDic.json')
        self.frase1 = None


    def entrada(self,frase=None):
        if frase == None:
            msg = str(input(":> "))
        msg = str(frase)
        msg = func.compResp(msg)
        print(msg)
        processedMsg = msg.lower()

        for acaos in self.acaod:
            if acaos in msg:
                msg = msg.replace(acaos,self.acaod[acaos])

        if 'executar' in processedMsg:
            try:
                programa = msg.replace('executar ','')
            except AttributeError:
                return 0, 'Nenhum programa informado'
            print(programa)
            return 1, programa
        else:
            if processedMsg == "alt f4":
                return 0, True
            return 0, processedMsg
    def pensa(self,resp,value):
        if resp in self.resplist:
            if self.nameUser == None:
                return 'Oi, qual é o seu nome? ' 
            else:
                return  'Olá '+self.nameUser
        if value == 1:
            programa = resp
            result = func.sistema(programa)
            return 'abrindo '+programa

        if len(self.botHistorico) > 0:
            if self.botHistorico[-1] == 'Oi, qual é o seu nome? ':
                name = self.userName(resp).title()
                self.nameUser = name
                return 'Olá '+ name

            if self.botHistorico[-1] == 'Informe a frase de entrada:':
                self.frase1 = resp
                return 'Informe a saida:'
            if self.botHistorico[-1] == 'Informe a saida:':
                frase2 = resp
                self.acaod[self.frase1] = frase2
                func.savJson('frDic.json',self.acaod)

                return 'Aprendido!'

            if self.botHistorico[-1] == 'informe a frase:':
                resultExc = None
                if resp != '':
                    try:
                        resultExc = self.acaod.pop(resp)
                    except KeyError:
                        resultExc = None
                if resultExc == None:
                    return 'a frase não foi excluida'
                else:
                    func.savJson('frDic.json',self.acaod)
                    return 'frase excluida'

        if 'aprende' in resp:
            return 'Informe a frase de entrada:'            

        if 'esquece' in resp:
            return 'informe a frase:'

        if resp in self.acaod:
            return self.acaod[resp]
        try:
            pResp = resp.replace('x','*')
            calc = str(eval(pResp))
            return calc

        except  ZeroDivisionError:
            return 'Erro divisão por zero'
        except NameError:
            pass
        except SyntaxError:
            pass
        if resp == '':
            return ''
        return 'Não entendi'
        

    def userName(self, resp):
        msglist = resp.split()
        name = msglist[-1]
        return name

    def resposta(self,msg):
        print(msg)
        if not 'Não entendi' in msg:
            self.botHistorico.append(msg)
from brain import brain
from outIn import OutIn

outin = OutIn()
class BotSpeaker(brain):
    def entrada(self, frase=None):
        msg = outin.escuta()
        return super().entrada(frase=msg)
    def resposta(self,msg):
        outin.fala(msg)
        super().resposta(msg)

Bot = BotSpeaker()

running = True
while running == True:

    value, processedUsResp = Bot.entrada()
    if processedUsResp == True:
        Bot.resposta('Fechando')
        running = False

    else:
        botResp = Bot.pensa(processedUsResp, value)
        Bot.resposta(botResp)
        
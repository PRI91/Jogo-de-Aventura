# Projeto 1 - Jogo de Aventura
# Um jogo de decisões onde eu terei que criar varios finais diferentes baseados nas respostas que forem dadas

# Chegar a finais diferentes na minha historia, de acordo com as respostas que eu passe para o programa

#Qual é o cenário : Eu estou numa guerra entre duas nações, onde existe 2 lados: LadoA e LadoB. Somente o LadoA irá vencer, e o LadoB irá

perder! Então eu tenho que tomar as decisões corretas para chegar até a vitória, que somente o lado LadoA conseguira!
class JogoDeAventura:
    def__init__(self):
       self.pergunta1 = 'você nasceu no norte ou sul (s/n?' #sul = LadoA, norte = LadoB
       self.pergunta2 = 'você prefere a espada ou escudo? (espada/escudo)' #espada = Lado1, escudo = Lado2
       self.pergunta3 = 'qual a sua especialidade? (linha de frente/tatico)' # linha de frente = Lado1, tático = Lado2
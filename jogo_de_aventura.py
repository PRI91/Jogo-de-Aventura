# Projeto 1 - Jogo de Aventura
# Um jogo de decisões onde eu terei que criar varios finais diferentes baseados nas respostas que forem dadas

# Chegar a finais diferentes na minha historia, de acordo com as respostas que eu passe para o programa

# Qual é o cenário : Eu estou numa guerra entre duas nações, onde existe 2 lados: LadoA e LadoB. Somente o LadoA irá vencer,
#  e o LadoB irá perder! então tenho que tomar as decisões corretas para chegar até a vitória, que somente o LadoA conseguira.
class JogoDeAventura:
    def_init_(self):
       self.pergunta1 = 'você nasceu no norte ou sul (s/n?' #sul = LadoA, norte = LadoB
       self.pergunta2 = 'você prefere a espada ou flexa? (espada/flexa)' #espada = Lado1, flexa = Lado2
       self.pergunta3 = 'qual a sua especialidade? (linha de frente/tatico)' # linha de frente = Lado1, tático = Lado2
       self.finalHistoria1 = 'Você será um heroi na linha de frente!'
       self.finalHistoria2 = 'Você sera um heroi protegendo todas as nossas tropas!'
       self.finalHistoria3 = 'Você irá se sacrificar na batalha!'
       self.finalHistoria4 = 'Você não é capaz de lutar nessa batalha!'


    def Iniciar(self):
        resposta1 = input(self.pergunta1)
        if resposta1 == 'n': 
            resposta1B = input(self.pergunta2)
            if resposta1B == 'espada':
                print(self.finalHistoria1)
            if resposta1B == 'flexa':
                print (self.finalHistoria2)    
        if resposta1 == 's':
            resposta1B = input(self.pergunta3)
            if resposta1B == 'linha de frente':
                print(self.finalHistoria3)
            if resposta1B == 'tatico':
                print(self.finalHistoria4)

jogo = JogoDeAventura()
jogo Iniciar()               
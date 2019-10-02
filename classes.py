class Pessoa:
    nome = ""
    idade = -1
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def comer(self, comida):
        print('Comendo '', end = ' ')

class Estudante(Pessoa):
    curso = ""
    def __init__(self, curso, nome, idade):
        super().__init__(nome, idade)
        self.curso = curso
    def comer(self, comida):
        print('Estou no RU', end = '')
        super().comer(comida)

bruno = Estudante('Engenharia da Computação', 'Bruno', 24)
#print(type(bruno))
#print(isinstance(bruno,Estudante))
bruno.comer('Feijão')
ana = Pessoa('Ana', 20)
ana.comer('Arroz')

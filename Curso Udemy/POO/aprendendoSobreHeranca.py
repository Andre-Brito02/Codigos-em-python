class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def falar_nome_classe(self):
        print(f"{self.nome} {self.sobrenome} {self.__class__.__name__}")

class Cliente(Pessoa):
    def falar_nome_classe(self):
        print(f"Nome e sobrenome: {self.nome} {self.sobrenome}")

class Aluno(Pessoa):
    ...

c1 = Cliente("André", "Brito")
c1.falar_nome_classe()
a1 = Aluno("Harry", "Porco")
a1.falar_nome_classe()


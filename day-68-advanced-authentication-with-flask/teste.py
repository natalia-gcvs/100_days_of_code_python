class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.sala = 5

    def greet_aluno(self):
        return f'Hi {self.nome}'



novo_aluno = Aluno(nome='Natalia')

print(novo_aluno.greet_aluno())

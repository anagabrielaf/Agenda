class Contato:
    def __init__(self, nome, telefone, endereco, aniversario):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.aniversario = aniversario

    def __str__(self):
        return f"{self.nome}, {self.telefone}, {self.endereco}, {self.aniversario}"

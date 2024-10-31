from contato import Contato
from gerenciador_arquivos import GerenciadorArquivos
from notificador import Notificador

class Agenda:
    def __init__(self):
        self.contatos = GerenciadorArquivos.carregar_contatos()

    def adicionar(self, nome, telefone, endereco, aniversario):
        if any(c.nome.lower() == nome.lower() for c in self.contatos):
            raise ValueError("Erro: Já existe um contato com esse nome.")
        self.contatos.append(Contato(nome, telefone, endereco, aniversario))
        GerenciadorArquivos.salvar_contatos(self.contatos)

    def apaga(self, nome):
        for contato in self.contatos:
            if contato.nome.lower() == nome.lower():
                self.contatos.remove(contato)
                GerenciadorArquivos.salvar_contatos(self.contatos)
                return f"Contato {nome} removido."
        raise ValueError("Contato não encontrado.")

    def altera(self, nome, telefone=None, endereco=None, aniversario=None):
        for contato in self.contatos:
            if contato.nome.lower() == nome.lower():
                if telefone:
                    contato.telefone = telefone
                if endereco:
                    contato.endereco = endereco
                if aniversario:
                    contato.aniversario = aniversario
                GerenciadorArquivos.salvar_contatos(self.contatos)
                return f"Contato {nome} alterado."
        raise ValueError("Contato não encontrado.")

    def lista(self):
        return [f"{i}: {contato}" for i, contato in enumerate(self.contatos)]

    def ordenar_contatos(self):
        self.contatos.sort(key=lambda c: c.nome)

    def verificar_aniversarios(self):
        return Notificador.verificar_aniversarios(self.contatos)

    def tamanho(self):
        return len(self.contatos)

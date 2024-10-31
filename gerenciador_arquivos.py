import csv

class GerenciadorArquivos:
    @staticmethod
    def salvar_contatos(contatos, filename='contatos.csv'):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for contato in contatos:
                writer.writerow([contato.nome, contato.telefone, contato.endereco, contato.aniversario])

    @staticmethod
    def carregar_contatos(filename='contatos.csv'):
        contatos = []
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    contatos.append(Contato(row[0], row[1], row[2], row[3]))
        except FileNotFoundError:
            pass
        return contatos

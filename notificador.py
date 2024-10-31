from datetime import datetime

class Notificador:
    @staticmethod
    def verificar_aniversarios(contatos):
        hoje = datetime.now().strftime("%d/%m")
        aniversarios = [c.nome for c in contatos if c.aniversario[3:] == hoje]
        return aniversarios

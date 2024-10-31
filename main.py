from agenda import Agenda

def menu():
    agenda = Agenda()

    while True:
        aniversarios = agenda.verificar_aniversarios()
        if aniversarios:
            print("Aniversariantes de hoje: " + ", ".join(aniversarios))
        
        print("\nAgenda de Contatos")
        print(f"Tamanho da agenda: {agenda.tamanho()}")
        print("1. Adicionar Contato")
        print("2. Apagar Contato")
        print("3. Alterar Contato")
        print("4. Listar Contatos")
        print("5. Ordenar por Nome")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")
        try:
            if opcao == '1':
                nome = input("Nome: ")
                telefone = input("Telefone: ")
                endereco = input("Endereço: ")
                aniversario = input("Data de Aniversário (dd/mm/aaaa): ")
                agenda.adicionar(nome, telefone, endereco, aniversario)
            elif opcao == '2':
                nome = input("Nome do contato a ser apagado: ")
                print(agenda.apaga(nome))
            elif opcao == '3':
                nome = input("Nome do contato a ser alterado: ")
                telefone = input("Novo Telefone (deixe em branco para não alterar): ")
                endereco = input("Novo Endereço (deixe em branco para não alterar): ")
                aniversario = input("Nova Data de Aniversário (deixe em branco para não alterar): ")
                print(agenda.altera(nome, telefone if telefone else None, endereco if endereco else None, aniversario if aniversario else None))
            elif opcao == '4':
                contatos_listados = agenda.lista()
                for contato in contatos_listados:
                    print(contato)
            elif opcao == '5':
                agenda.ordenar_contatos()
                print("Contatos ordenados por nome.")
            elif opcao == '6':
                break
            else:
                print("Opção inválida.")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    menu()

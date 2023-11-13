from decimal import *

class View():
    def inicio(self):
        return self.menu()

    def menu(self):
        print("M E N U")
        print("1. Popular a tabela de Deputados")
        print("2. Popular a tabela de Orgãos")
        print("3. Popular a tabela de Eventos")
        print("4. Popular a tabela de PedidosLicitação")
        print("9. Sair")
        opcao = int(input("Digite a opcao desejada : "))
        return opcao

    def imprimeStatus(self, status):
        if (status == 1):
            print("Carga realizada com sucesso!")
        else:
            print(status)


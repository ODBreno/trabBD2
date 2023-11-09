from decimal import *

class View():
    def inicio(self):
        return self.menu()

    def menu(self):
        print("M E N U")
        print("1. Popular a tabela de Deputados")
        print("9. Sair")
        opcao = int(input("Digite a opcao desejada : "))
        return opcao

    def imprimeStatus(self, status):
        if (status == 1):
            print("Carga realizada com sucesso!")
        else:
            print(status)


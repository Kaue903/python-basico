#  Texto especial para usar no projeto (abaixo)
#  𝕊𝕒𝕓𝕠𝕣 𝕖𝕩𝕡𝕣𝕖𝕤𝕤

import os

class Restaurante:

    def __init__(self, nome, categoria):
            self.nome = nome
            self.categoria = categoria
            self.activo = False



    def alternar_estado(self):
        self.activo = not self.activo



    def __str__(self):
         status = "ativado" if self.activo else "desativado"
         return f"{self.nome.ljust(20)} | {self.categoria.ljust(20)} | {status}"

class SaborExpress:


    def __init__(self):
         self.restaurantes = [
                Restaurante("Praça", "Japonesa"),
                Restaurante("Pizza suprema", "Pizza"),
                Restaurante("Cantina", "Italiana"),
         ]


    def cadastrar_restaurante(self, nome, categoria):
        novo_restaurante = Restaurante(nome, categoria)
        self.restaurantes.append(novo_restaurante)
        return novo_restaurante


    def buscar_restaurante(self, nome):
        for restaurante in self.restaurantes:
            if restaurante.nome == nome:
                return restaurante
        return None


    def listar_restaurantes(self):
        return self.restaurantes


class Menu:

    def __init__(self):
        self.app = SaborExpress()


# ------------Método para exibir o menu principal --------
    def exibir_subtitulo(self, texto):
        os.system("cls")
        linha = "-" * len(texto)
        print(linha)
        print(texto)
        print(linha)
        print()

    def exibir_nome_do_programa(self):
        print("𝕊𝕒𝕓𝕠𝕣 𝕖𝕩𝕡𝕣𝕖𝕤𝕤")


    def exibir_opcoes(self):
        print("1. Cadastrar restaurante")
        print("2. Listar restaurantes")
        print("3. Alternar estado do restaurante")
        print("4. Sair")


# ------- Método de ação (chamdos a partir do menu) -------------

    def cadastrar_novo_restaurante(self):
        self.exibir_subtitulo("Cadastro de novos Restaurantes")
        nome = input("Digite o nome do restaurante que deseja cadastrar: ")
        categoria = input("Digite o nome da categoria do restaurante {nome}: ")

        self.app.cadastrar_restaurante(nome, categoria)
        print(f"O restaurante {nome} foi cadastrado com sucesso!")

        self.voltar_ao_menu_principal()


    def alternar_estado_restaurante(self):
        self.exibir_subtitulo("Alternar estado do restaurante")
        nome_restaurante = input("Digite o nome do restaurante que deseja alternar o estado: ")

        restaurante = self.app.buscar_restaurante(nome_restaurante)
        if restaurante:
            restaurante.alternar_estado()
            status = "ativado" if restaurante.activo else "desativado"
            print(f"O estado do restaurante {nome_restaurante} foi {status} com sucesso!")
        else:
            print(f"Restaurante {nome_restaurante} não encontrado.")

        self.voltar_ao_menu_principal()
        

    def listar_restaurantes(self):
        self.exibir_subtitulo("Listando os Restaurantes\n")
        print(f"{'Nome'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'}")

        for restaurante in self.app.listar_restaurantes():
            print(restaurante)

        self.voltar_ao_menu_principal()

    def finalizar_app(self):
        self.exibir_subtitulo("Finalizando o programa...\n")


    def opcao_invalida(self):
        print("Opção inválida. Por favor, tente novamente.\n")
        self.voltar_ao_menu_principal()

    def voltar_ao_menu_principal(self):
        input("\nPressione uma tecla para voltar ao menu principal...")
        self.main()


    def escolher_opcao(self):
        try:
            opcao_escolhida = int(input("Escolha uma opção: "))

            if opcao_escolhida == 1:
                self.cadastrar_novo_restaurante()
            elif opcao_escolhida == 2:
                self.listar_restaurantes()
            elif opcao_escolhida == 3:
                self.alternar_estado_restaurante()
            elif opcao_escolhida == 4:
                self.finalizar_app()
            else:
                self.opcao_invalida()
        except ValueError:
            self.opcao_invalida()

    def main(self):
        os.system("cls")
        self.exibir_nome_do_programa()
        self.exibir_opcoes()
        self.escolher_opcao()

if __name__ == "__main__":
    menu = Menu()
    menu.main()
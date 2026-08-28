import os
import sqlite3

# Variável com o nome do BD a ser criado
CAMINHO_BANCO = "jogos.db"


def exibir_cabecalho(texto):
    os.system("cls")

    linha = "*" * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()


# Função para inicializar o banco de dados
def inicializar_banco():
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jogos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            plataforma TEXT NOT NULL,
            zerado BOOLEAN NOT NULL DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()


def listar_jogos():
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()

    cursor.execute("SELECT titulo, plataforma, zerado FROM jogos")
    jogos = cursor.fetchall()

    conn.close()

    if not jogos:
        print("Nenhum jogo cadastrado ainda!\n")
        return

    print(f"{'Titulo'.ljust(25)} | {'Plataforma'.ljust(12)} | Status")
    print("-" * 55)

    for titulo, plataforma, zerado in jogos:
        status = "zerado" if zerado else "jogando"
        print(f"{titulo.ljust(25)} | {plataforma.ljust(12)} | {status}")

    print()


def adicionar_jogo(titulo, plataforma):
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO jogos (titulo, plataforma, zerado) VALUES (?, ?, ?)",
        (titulo, plataforma, False)
    )

    conn.commit()
    conn.close()


def marcar_como_zerado(titulo):
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE jogos SET zerado = ? WHERE titulo = ?",
        (True, titulo)
    )

    encontrou = cursor.rowcount > 0

    conn.commit()
    conn.close()

    return encontrou


# Função para deletar um jogo
def deletar_jogo(titulo):
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM jogos WHERE titulo = ?",
        (titulo,)
    )

    encontrou = cursor.rowcount > 0

    conn.commit()
    conn.close()

    return encontrou

def buscar_jogo(titulo):
    # Busca um jogo pelo titulo exato (outra forma sem usar id). Usado antes de fazer a edição.
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT titulo, plataforma FROM jogos WHERE titulo = ?",
        (titulo,),
    )

    jogo = cursor.fetchone()

    conn.close()
    return jogo


def atualizar_jogo(titulo_atual, novo_titulo, nova_plataforma):
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE jogos SET titulo = ?, plataforma = ? WHERE titulo = ?",
        (novo_titulo, nova_plataforma, titulo_atual),
    )

    encontrou = cursor.rowcount > 0

    conn.commit()
    conn.close()

    return encontrou


def exibir_menu():
    exibir_cabecalho("🎮 GameVault")

    print("1. Adicionar jogo")
    print("2. Listar jogos")
    print("3. Marcar jogo como zerado")
    print("4. Deletar jogo")
    print("5. Editar jogo")
    print("6. Sair")
    print()


def pausar():
    input("Pressione Enter para voltar ao menu...")


def main():
    inicializar_banco()

    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ")

        # Adicionar jogo
        if opcao == "1":
            exibir_cabecalho("Adicionar jogo")

            titulo = input("Título do jogo: ")
            plataforma = input("Plataforma: ")

            adicionar_jogo(titulo, plataforma)

            print(f"\n'{titulo}' adicionado com sucesso!")

            pausar()

        # Listar jogos
        elif opcao == "2":
            exibir_cabecalho("Seus jogos")

            listar_jogos()

            pausar()

        # Marcar como zerado
        elif opcao == "3":
            exibir_cabecalho("Marcar como zerado")

            titulo = input("Título do jogo que zerou: ")

            if marcar_como_zerado(titulo):
                print(f"\n'{titulo}' marcado como zerado!")
            else:
                print(f"\n'{titulo}' não encontrado!")
                print("Confira se digitou corretamente.")

            pausar()

        # Deletar jogo
        elif opcao == "4":
            exibir_cabecalho("Deletar jogo")

            titulo = input("Título do jogo que deseja deletar: ")

            if deletar_jogo(titulo):
                print(f"\n'{titulo}' deletado com sucesso!")
            else:
                print(f"\n'{titulo}' não encontrado!")
                print("Confira se digitou corretamente.")

            pausar()

        #Editar dados
        elif opcao == "5":
            exibir_cabecalho("Editar jogo")

            titulo = input("Título do jogo que deseja atualizar: ")

            # Localiza o jogo correto para atualizar
            jogo = buscar_jogo(titulo)

            # Buscou jogo que não existe
            if jogo is None:
                print(f"\n'{titulo}' não encontrado!")
                print("Confira se digitou os dados corretamente.")

            else:
                titulo_atual, plataforma_atual = jogo
                print(f"\nJogo encontrado: {titulo_atual} ({plataforma_atual})")

                # Captura os novos títulos e plataformas
                novo_titulo = input(f"Novo título (Enter para manter '{titulo_atual}'): ")
                nova_plataforma = input(f"Nova plataforma (Enter para manter '{plataforma_atual}'): ")

                # Se a pessoa apertou Enter, mantém o valor atual
                if novo_titulo.strip() == "":
                    novo_titulo = titulo_atual
                if nova_plataforma.strip() == "":
                    nova_plataforma = plataforma_atual

                # Confirma a atualização
                if atualizar_jogo(titulo_atual, novo_titulo, nova_plataforma):
                    print(f"\nJogo atualizado com sucesso: '{novo_titulo}' ({nova_plataforma})")
                else:
                    print("\nNão foi possível atualizar o jogo.")

            pausar()

        # Sair
        elif opcao == "6":
            print("Até a próxima! 😁")
            break

        # Opção inválida
        else:
            print("Opção inválida! Escolha um número de 1 a 5.")
            pausar()


# Inicia o programa
if __name__ == "__main__":
    main()
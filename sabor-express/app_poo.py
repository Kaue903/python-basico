# Sabor Express - Versão Orientada a Objetos com SQLite
# Sistema de cadastro e gerenciamento de restaurantes

import os
import sqlite3


# ============================================================
# CLASSE PRINCIPAL DO SISTEMA
# Responsável pela comunicação com o banco de dados
# ============================================================

class SaborExpress:

    # Construtor
    def __init__(self, caminho_banco="restaurantes.db"):
        self.caminho_banco = caminho_banco
        self.inicializar_banco()

    # Cria o banco e a tabela caso ainda não existam
    def inicializar_banco(self):
        conn = sqlite3.connect(self.caminho_banco)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS restaurantes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                categoria TEXT NOT NULL,
                ativo BOOLEAN NOT NULL DEFAULT 0
            )
        """)

        # Insere os restaurantes iniciais somente se a tabela estiver vazia
        cursor.execute("SELECT COUNT(*) FROM restaurantes")
        total = cursor.fetchone()[0]

        if total == 0:
            restaurantes_iniciais = [
                ("Praça", "Japonesa", False),
                ("Pizza Suprema", "Pizza", True),
                ("Cantina", "Italiano", False)
            ]

            cursor.executemany(
                """
                INSERT INTO restaurantes
                (nome, categoria, ativo)
                VALUES (?, ?, ?)
                """,
                restaurantes_iniciais
            )

        conn.commit()
        conn.close()

    # ========================================================
    # CADASTRAR RESTAURANTE
    # ========================================================

    def cadastrar_restaurante(self, nome, categoria):
        try:
            conn = sqlite3.connect(self.caminho_banco)
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO restaurantes
                (nome, categoria, ativo)
                VALUES (?, ?, ?)
                """,
                (nome, categoria, False)
            )

            conn.commit()
            conn.close()

            return True

        except sqlite3.Error as erro:
            print(f"❌ Erro ao cadastrar restaurante: {erro}")
            return False

    # ========================================================
    # BUSCAR ESTADO DO RESTAURANTE
    # ========================================================

    def buscar_estado(self, nome):
        conn = sqlite3.connect(self.caminho_banco)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT ativo FROM restaurantes WHERE nome = ?",
            (nome,)
        )

        resultado = cursor.fetchone()

        conn.close()

        if resultado is not None:
            return resultado[0]

        return None

    # ========================================================
    # ALTERNAR ESTADO
    # ========================================================

    def alternar_estado(self, nome):
        estado_atual = self.buscar_estado(nome)

        if estado_atual is None:
            return None

        novo_estado = not estado_atual

        conn = sqlite3.connect(self.caminho_banco)
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE restaurantes
            SET ativo = ?
            WHERE nome = ?
            """,
            (novo_estado, nome)
        )

        conn.commit()
        conn.close()

        return novo_estado

    # ========================================================
    # LISTAR RESTAURANTES
    # ========================================================

    def listar_restaurantes(self):
        conn = sqlite3.connect(self.caminho_banco)
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT nome, categoria, ativo
            FROM restaurantes
            ORDER BY nome
            """
        )

        restaurantes = cursor.fetchall()

        conn.close()

        return restaurantes

    # ========================================================
    # VERIFICAR SE RESTAURANTE EXISTE
    # ========================================================

    def restaurante_existe(self, nome):
        conn = sqlite3.connect(self.caminho_banco)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id FROM restaurantes WHERE nome = ?",
            (nome,)
        )

        resultado = cursor.fetchone()

        conn.close()

        return resultado is not None

    # ========================================================
    # ATUALIZAR RESTAURANTE
    # UPDATE
    # ========================================================

    def atualizar_restaurante(
        self,
        nome_atual,
        novo_nome,
        nova_categoria
    ):
        try:
            conn = sqlite3.connect(self.caminho_banco)
            cursor = conn.cursor()

            cursor.execute(
                """
                UPDATE restaurantes
                SET nome = ?, categoria = ?
                WHERE nome = ?
                """,
                (
                    novo_nome,
                    nova_categoria,
                    nome_atual
                )
            )

            encontrou = cursor.rowcount > 0

            conn.commit()
            conn.close()

            return encontrou

        except sqlite3.Error as erro:
            print(f"❌ Erro ao atualizar restaurante: {erro}")
            return False

    # ========================================================
    # EXCLUIR RESTAURANTE
    # ========================================================

    def excluir_restaurante(self, nome):
        conn = sqlite3.connect(self.caminho_banco)
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM restaurantes WHERE nome = ?",
            (nome,)
        )

        conn.commit()
        conn.close()


# ============================================================
# CLASSE MENU
# Responsável pela interação com o usuário
# ============================================================

class Menu:

    # Construtor
    def __init__(self):
        self.app = SaborExpress()

    # ========================================================
    # EXIBIR SUBTÍTULO
    # ========================================================

    def exibir_subtitulo(self, texto):
        os.system("cls")

        linha = "═" * len(texto)

        print(f"╔{linha}╗")
        print(f"║{texto}║")
        print(f"╚{linha}╝")
        print()

    # ========================================================
    # NOME DO PROGRAMA
    # ========================================================

    def exibir_nome_do_programa(self):
        print("""
╔══════════════════════════════════════╗
║          🍴 SABOR EXPRESS 🍴        ║
║     Sistema de Restaurantes 🏪      ║
╚══════════════════════════════════════╝
        """)

    # ========================================================
    # OPÇÕES DO MENU
    # ========================================================

    def exibir_opcoes(self):
        print("📋 MENU PRINCIPAL")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("📝 1. Cadastrar restaurante")
        print("📋 2. Listar restaurantes")
        print("🔄 3. Alternar estado do restaurante")
        print("✏️  4. Atualizar restaurante")
        print("🗑️  5. Excluir restaurante")
        print("🚪 6. Sair")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print()

    # ========================================================
    # CADASTRAR NOVO RESTAURANTE
    # ========================================================

    def cadastrar_novo_restaurante(self):
        self.exibir_subtitulo(
            "🍽️ Cadastro de novo restaurante"
        )

        nome = input(
            "🏪 Digite o nome do restaurante: "
        )

        categoria = input(
            f"🍕 Digite a categoria do restaurante {nome}: "
        )

        sucesso = self.app.cadastrar_restaurante(
            nome,
            categoria
        )

        if sucesso:
            print(
                f"\n✅ O restaurante '{nome}' "
                f"foi cadastrado com sucesso!"
            )

        self.voltar_ao_menu_principal()

    # ========================================================
    # ALTERNAR ESTADO DO RESTAURANTE
    # ========================================================

    def alternar_estado_do_restaurante(self):
        self.exibir_subtitulo(
            "🔄 Alterando estado do restaurante"
        )

        nome = input(
            "🏪 Digite o nome do restaurante: "
        )

        novo_estado = self.app.alternar_estado(nome)

        if novo_estado is None:
            print(
                "\n❌ O restaurante não foi encontrado!"
            )

        else:
            status = (
                "ativado 🟢"
                if novo_estado
                else "desativado 🔴"
            )

            print(
                f"\n✅ O restaurante '{nome}' "
                f"foi {status} com sucesso!"
            )

        self.voltar_ao_menu_principal()

    # ========================================================
    # LISTAR RESTAURANTES
    # ========================================================

    def listar_restaurantes(self):
        self.exibir_subtitulo(
            "📋 Lista de restaurantes"
        )

        restaurantes = self.app.listar_restaurantes()

        if restaurantes:

            print(
                f"{'🏪 Restaurante'.ljust(21)} | "
                f"{'🍕 Categoria'.ljust(20)} | "
                f"Status"
            )

            print("─" * 65)

            for nome, categoria, ativo in restaurantes:

                status = (
                    "🟢 Ativado"
                    if ativo
                    else "🔴 Desativado"
                )

                print(
                    f"{nome.ljust(21)} | "
                    f"{categoria.ljust(20)} | "
                    f"{status}"
                )

        else:
            print(
                "📭 Nenhum restaurante cadastrado."
            )

        self.voltar_ao_menu_principal()

    # ========================================================
    # ATUALIZAR RESTAURANTE
    # ========================================================

    def atualizar_restaurante(self):
        self.exibir_subtitulo(
            "✏️ Atualizar restaurante"
        )

        restaurantes = self.app.listar_restaurantes()

        if not restaurantes:
            print(
                "📭 Nenhum restaurante cadastrado "
                "para atualizar."
            )

            self.voltar_ao_menu_principal()
            return

        print("🏪 Restaurantes cadastrados:")
        print("─" * 45)

        for nome, categoria, ativo in restaurantes:

            status = (
                "🟢 Ativado"
                if ativo
                else "🔴 Desativado"
            )

            print(
                f"• {nome} | {categoria} | {status}"
            )

        print()

        nome_atual = input(
            "🔎 Digite o nome do restaurante "
            "que deseja atualizar: "
        )

        # Verifica se existe
        if not self.app.restaurante_existe(nome_atual):

            print(
                "\n❌ O restaurante não foi encontrado!"
            )

            self.voltar_ao_menu_principal()
            return

        print("\n✏️ Informe os novos dados:")

        novo_nome = input(
            "🏪 Novo nome: "
        )

        nova_categoria = input(
            "🍕 Nova categoria: "
        )

        sucesso = self.app.atualizar_restaurante(
            nome_atual,
            novo_nome,
            nova_categoria
        )

        if sucesso:

            print(
                "\n✅ Restaurante atualizado "
                "com sucesso!"
            )

            print(
                f"🏪 Novo nome: {novo_nome}"
            )

            print(
                f"🍕 Nova categoria: {nova_categoria}"
            )

        else:
            print(
                "\n❌ Não foi possível atualizar "
                "o restaurante."
            )

        self.voltar_ao_menu_principal()

    # ========================================================
    # EXCLUIR RESTAURANTE
    # ========================================================

    def excluir_restaurante(self):
        self.exibir_subtitulo(
            "🗑️ Excluir restaurante"
        )

        restaurantes = self.app.listar_restaurantes()

        if not restaurantes:

            print(
                "📭 Nenhum restaurante cadastrado "
                "para excluir."
            )

            self.voltar_ao_menu_principal()
            return

        print("🏪 Restaurantes cadastrados:")
        print("─" * 40)

        for nome, categoria, _ in restaurantes:
            print(
                f"• {nome} ({categoria})"
            )

        print()

        nome = input(
            "🔎 Digite o nome do restaurante "
            "que deseja excluir: "
        )

        if self.app.restaurante_existe(nome):

            confirmacao = input(
                f'\n⚠️ Tem certeza que deseja excluir '
                f'o restaurante "{nome}"? (s/n): '
            )

            if confirmacao.lower() == "s":

                self.app.excluir_restaurante(nome)

                print(
                    f"\n✅ O restaurante '{nome}' "
                    f"foi excluído com sucesso!"
                )

            else:

                print(
                    "\n↩️ Exclusão cancelada."
                )

        else:

            print(
                "\n❌ O restaurante não foi encontrado!"
            )

        self.voltar_ao_menu_principal()

    # ========================================================
    # FINALIZAR APLICATIVO
    # ========================================================

    def finalizar_app(self):
        self.exibir_subtitulo(
            "👋 Finalizando o Sabor Express"
        )

        print(
            "🍴 Obrigado por utilizar o "
            "Sabor Express!"
        )

        print(
            "✨ Até a próxima!"
        )

    # ========================================================
    # OPÇÃO INVÁLIDA
    # ========================================================

    def opcao_invalida(self):
        print(
            "\n❌ Opção inválida!"
        )

        self.voltar_ao_menu_principal()

    # ========================================================
    # VOLTAR AO MENU PRINCIPAL
    # ========================================================

    def voltar_ao_menu_principal(self):
        input(
            "\n↩️ Pressione ENTER para voltar "
            "ao menu principal..."
        )

        self.main()

    # ========================================================
    # ESCOLHER OPÇÃO
    # ========================================================

    def escolher_opcao(self):

        try:

            opcao_escolhida = int(
                input("👉 Escolha uma opção: ")
            )

            if opcao_escolhida == 1:

                self.cadastrar_novo_restaurante()

            elif opcao_escolhida == 2:

                self.listar_restaurantes()

            elif opcao_escolhida == 3:

                self.alternar_estado_do_restaurante()

            elif opcao_escolhida == 4:

                self.atualizar_restaurante()

            elif opcao_escolhida == 5:

                self.excluir_restaurante()

            elif opcao_escolhida == 6:

                self.finalizar_app()

            else:

                self.opcao_invalida()

        except ValueError:

            self.opcao_invalida()

    # ========================================================
    # FUNÇÃO PRINCIPAL
    # ========================================================

    def main(self):

        os.system("cls")

        self.exibir_nome_do_programa()

        self.exibir_opcoes()

        self.escolher_opcao()


# ============================================================
# PONTO DE ENTRADA DO PROGRAMA
# ============================================================

if __name__ == "__main__":

    menu = Menu()

    menu.main()
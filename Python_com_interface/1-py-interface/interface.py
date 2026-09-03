# Exemplo de Interface — versão orientada a objetos
# Janela simples: digita um texto, clica no botão, o texto aparece no rótulo.

import tkinter as tk

#Classe principal
class InterfaceExemplo:
    #Método construtor
    def __init__(self):
        self.janela = tk.Tk()  # Cria a janela principal
        self.janela.title("Exemplo de Interface")  # Define o título da janela
        self.janela.geometry("400x150")  # Define o tamanho da janela
        self.janela.configure(bg="lightgray")  # Define a cor de fundo da janela
        self.criar_widgets()  # Chama o método para criar os widgets

    # Montar todos os elementos visuais da tela
    def criar_widgets(self):
        # Caixa de entrada ("Entry") ou input onde o usuário digita o texto
        self.caixa_texto = tk.Entry(self.janela, width=60)
        self.caixa_texto.pack(pady=10)  # Adiciona a caixa de entrada à janela

        # Botão que dispara mostrar_mensagem() ao ser clicado
        self.botao = tk.Button(self.janela, text="Mostrar texto", bg="lightblue", command=self.mostrar_mensagem)
        self.botao.pack(pady=5)  # Adiciona o botão à janela

        # Rótulo ("Label") onde o texto digitado será exibido
        self.label_resultado = tk.Label(self.janela, text="",fg="red", bg="grey")
        self.label_resultado.pack(pady=10)  # Adiciona o rótulo à janela

    # Método que exibe o texto digitado no rótulo
    def mostrar_mensagem(self):
        texto = self.caixa_texto.get()
        self.label_resultado.config(text=texto)

    # Inicia o loop principal da interface
    def executar(self):
        self.janela.mainloop()  # Mantém a janela aberta e aguardando interações

#Conecta a classe principal com a execução do programa
if __name__ == "__main__":
    app = InterfaceExemplo()  # Cria uma instância da classe InterfaceExemplo
    app.executar()  # Chama o método executar para iniciar a interface 
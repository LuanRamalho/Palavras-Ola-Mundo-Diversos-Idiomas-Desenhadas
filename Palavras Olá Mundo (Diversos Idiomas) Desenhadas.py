import tkinter as tk

def desenhar_texto():
    # Criação da janela principal
    janela = tk.Tk()
    janela.title("Olá Mundo em vários idiomas")
    janela.geometry("500x400")

    # Criação do canvas
    canvas = tk.Canvas(janela, width=500, height=400, bg="#f0f8ff")
    canvas.pack()

    # Desenhando os textos nas coordenadas específicas
    textos = [
        ("Português: Olá Mundo", 40, 50, "#ff4500"),
        ("Inglês: Hello World", 40, 100, "#1e90ff"),
        ("Espanhol: Hola Mundo", 40, 150, "#32cd32"),
        ("Francês: Bonjour Monde", 40, 200, "#8a2be2"),
        ("Italiano: Ciao Mondo", 40, 250, "#ff1493"),
        ("Alemão: Hallo Welt", 40, 300, "#ffa500"),
    ]

    for texto, x, y, cor in textos:
        canvas.create_text(x, y, text=texto, anchor="w", font=("Arial", 14, "bold"), fill=cor)

    # Execução da janela principal
    janela.mainloop()

# Chamando a função para desenhar os textos
desenhar_texto()

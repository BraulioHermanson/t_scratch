import tkinter as tk

janela = tk.Tk()
janela.title("Exercicio Botao")

var_promocoes = tk.IntVar()
checkbox_promocoes = tk.Checkbutton(text = "Deseja receber e-mail promocionais?",variable = var_promocoes)
checkbox_promocoes.grid(row=0,column=0)

var_politicas = tk.IntVar()
checkbox_politicias = tk.Checkbutton(text="Aceitar Termos de uso e politicas de privacidade",variable=var_politicas)
checkbox_politicias.grid(row=1,column=0)

def enviar():
    if var_promocoes.get():
        print('Usuario deseja receber promocoes')
    else:
        print('Usuario NAO deseja receber promocoes')
    if var_politicas.get():
        print('Usuario concordou com os termos de usos e politicas de privacidade')
    else:
        print('Usuario NAO concordou')

botao_enviar = tk.Button(text="Enviar", command =enviar)
botao_enviar.grid(row=2,column=0)

janela.mainloop()
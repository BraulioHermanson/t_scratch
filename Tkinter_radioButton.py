import tkinter as tk

janela = tk.Tk()
janela.title("radiobutton")

var_aviao = tk.StringVar(value = "Vazio")

def enviar():
    print(var_aviao.get())

botao_classeeconomica = tk.Radiobutton(text = "Classe Economica",variable= var_aviao,value ="Classe Economica" , command =enviar)
botao_classeexecutiva = tk.Radiobutton(text = "Classe Executiva",variable= var_aviao,value ="Classe Executiva", command =enviar)
botao_primeiraclasse = tk.Radiobutton(text = "Primeira Classe",variable= var_aviao,value ="Primeira Classe", command =enviar)

botao_classeeconomica.grid(row=0,column=0)
botao_classeexecutiva.grid(row=0,column=1)
botao_primeiraclasse .grid(row=0,column=2)



# botao_enviar = tk.Button(text="Enviar", command =enviar)
# botao_enviar.grid(row=1,column=0)


janela.mainloop()
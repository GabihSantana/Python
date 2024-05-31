from tkinter import *
#import tkinter as tk
from tkinter import messagebox 

tela = Tk()
tela.geometry("500x200")
tela.title("Entrys")

# Declarando as strings para armazenar o conteúdo
name_var = StringVar()
senha_var = StringVar()

# Função para mostrar o resultado
def enviar():
    nome = name_var.get()
    senha = senha_var.get()

    print("O nome é: " + nome)
    print("A senha é: " + senha)

    name_var.set("")
    senha_var.set("")

# Criando o label para o entry de nome
label_nome = Label(tela, text = 'Usuário', font=('Arial', 10, 'bold'))
# Entry:
entry_name = Entry(tela, textvariable=name_var, font=('Arial', 10, 'bold'))

label_senha = Label(tela, text = 'Senha', font=('Arial', 10, 'bold'))
entry_senha = Entry(tela, textvariable=senha_var, font=('Arial', 10, 'bold'), show='*')

# Botão para chamar a função enviar
sub_btn = Button(tela, text='Submit', command= enviar) #command > função
messagebox.askquestion("askquestion", "Are you sure?")

# Posicionando na tela
label_nome.grid(row = 0, column = 0)
entry_name.grid(row=0, column=1)

label_senha.grid(row=1, column=0)
entry_senha.grid(row=1, column=1)

sub_btn.grid(row = 2, column=3)

tela.mainloop()
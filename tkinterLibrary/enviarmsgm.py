from tkinter import *
from tkinter import messagebox 
import pywhatkit
import re

root = Tk()
root.geometry("500x310")
root.title("Agende uma mensagem")
root.config(bg="#F28585", pady=20, padx=20)

num_var = StringVar()
msg_var = StringVar()
hr_var = IntVar()
min_var = IntVar()

def enviar_msg(numero, mensagem, hora, minutos):
    num_celular = f"+55{numero}"
    pywhatkit.sendwhatmsg(num_celular, mensagem, hora, minutos)

def validacao():
    numero = num_var.get()
    message = msg_var.get()
    hora = hr_var.get()
    minutos = min_var.get()

    if numero and message and hora and minutos:
        celular = r"[0-9]{9}"
        poibidos = [r"\\", r"?", r":", r"<", r">", r"|", r"/", r"\"", r"*"]

        if re.match(celular, numero) == None:
            messagebox.showwarning(title="Invalido", message="Número invalido! Por favor, tente novamente.")
        for proib in poibidos:
            if proib in message:
                message = message.replace(proib, " ")

        enviar_msg(numero, message, hora, minutos)
        messagebox.showinfo(title="Status", message="Mensagem enviada com sucesso!")

    else:
        messagebox.showwarning(title="Invalido", message="Alguma informação está invalida, por favor, tente novamente")

    num_var.set("")
    msg_var.set("")
    hr_var.set("")
    min_var.set("")

frame = Frame(root, bg = '#F2C6C2', width=800, height=500, pady=15, padx=15)
frame.pack()

lbl_numero = Label(frame, text = "Insira o número: ", bg="#F2C6C2", font=("verdana", 10, "bold"))
entry_num = Entry(frame, textvariable=num_var, font=("verdana", 10, "bold"))

lbl_numero.place(relwidth=0.50, relheight=0.05)
entry_num.place(relx=0.50, rely = 0.0, relwidth=0.40, relheight=0.08)

lbl_mensagem = Label(frame, text = "Insira a mensagem: ", font=("verdana", 10, "bold"), bg="pink", pady=10)
entry_msg = Entry(frame, textvariable=msg_var, font=("verdana", 10, "bold"))

lbl_mensagem.place(rely=0.12, relwidth=0.50, relheight=0.05)
entry_msg.place(relx=0.50, rely = 0.12, relwidth=0.40, relheight=0.08)


lbl_hora = Label(frame, text = "Insira a hora: ", font=("verdana", 10, "bold"), bg="pink", pady=10)
entry_hora = Entry(frame, textvariable=hr_var, font=("verdana", 10, "bold"))
hr_var.set("")
#entry_hora.insert(0, "")

lbl_hora.place(rely = 0.24, relwidth=0.50, relheight=0.05)
entry_hora.place(relx=0.50, rely = 0.23, relwidth=0.40, relheight=0.08)

lbl_minuto= Label(frame, text = "Insira o minuto: ", font=("verdana", 10, "bold"), bg="pink", pady=10)
entry_minuto = Entry(frame, textvariable=min_var, font=("verdana", 10, "bold"))
min_var.set("")

lbl_minuto.place(rely = 0.34, relwidth=0.50, relheight=0.05)
entry_minuto.place(relx=0.50, rely = 0.33, relwidth=0.40, relheight=0.08)

btn_enviar = Button(frame, text='Enviar', command = validacao, pady=5, padx=5, cursor="heart")

btn_enviar.place(relx=0.30, rely = 0.50, relwidth=0.40, relheight=0.15)


#lbl_numero.grid(row=0, column=1)
#entry_num.grid(row=0, column=2)
#lbl_mensagem.grid(row=1, column=1)
#entry_msg.grid(row=1, column=2)
#lbl_hora.grid(row=3, column=1)
#entry_hora.grid(row=3, column=2)
#lbl_minuto.grid(row=4, column=1)
#entry_minuto.grid(row=4, column=2)
#btn_enviar.grid(row=5, column=3)

#


root.mainloop()
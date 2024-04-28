from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from PIL import ImageTk, Image

import string
import random

# cores 
cor0 = "#444466"     #cor pretp
cor1 = "#feffff"    #cor branca
cor2 = "#f05a43"     #cor vermelho


# Layout
janela = Tk()
janela.title('')
janela.geometry('255x360')
janela.configure(bg=cor1)


estilo = ttk.Style(janela)
estilo.theme_use('clam')



# frames de telas em cima e baixo

frame_cima = Frame(janela, width=295, height=50, bg=cor1, pady=0, padx=0,  relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=310, bg=cor1, pady=0, padx=0,  relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# FRAME EM CIMA cabeçalho icon e titulo e linha

app_nome =Label(frame_cima,text='GERADOR DE SENHAS', width=20, height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 16 bold'), bg=cor1, fg=cor0)
app_nome.place(x=35, y=2)

# ------------------- Colocando  imagem Icon ----------------

img = Image.open('icons8-cadeado-48.png')
img = img.resize((30, 30))         # tamanho da imagem
img = ImageTk.PhotoImage(img)

app_icon = Label(frame_cima, height=60, image=img, compound=LEFT, padx=10, relief='flat', anchor='nw', bg=cor1)
app_icon.place(x=2, y=0)


# ----------------------- LINHA
app_linha =Label(frame_cima,text='', width=295, height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 1'), bg=cor2, fg=cor2)
app_linha.place(x=0, y=35)

# ----------------------------------------- funçao gerar senha def -------------------------------------------------------------
def criar_senha():
    letra_maior = string.ascii_uppercase
    letra_menor = string.ascii_lowercase
    numeros = '123456789'
    
    global combinar

    # ---- letras maiuscula 
    if estado1.get() == letra_maior:
        combinar =   letra_maior
    else:
        pass
    # ---- letras minuscula
    
    if estado_2.get() == letra_menor:
        combinar = combinar + letra_menor
    else:
        pass
    # ---- numeros
    
    if estado_3.get() == numeros:
        combinar = combinar + numeros
    else:
        pass
    

    
    comprimento = int(spin.get())
    senha = "".join(random.sample(combinar, comprimento))


    
    app_senha['text'] = senha

    def copiar_senha():
        info = senha
        frame_baixo.clipboard_clear()
        frame_baixo.clipboard_append(info)

        messagebox.showinfo("Sucesso", "A senha foi copiada com sucesso")

    botao_copiar =Button(frame_baixo, command=copiar_senha, text='Copiar', width=7,  height=2,  relief='flat', overrelief='raised',  anchor='center', font=('Ivy 10 bold'), bg=cor0, fg=cor1)
    botao_copiar.grid(row=0, column=1,  sticky=NW, padx=5, pady=10, columnspan=1)






# FRAME DE BAIXO
app_senha =Label(frame_baixo,text='... ', width=20, height=2, padx=0, relief='solid', anchor='center', font=('Ivy 12 bold'), bg=cor1, fg=cor0)
app_senha.grid(row=0, column=0, columnspan=1, sticky=NSEW, padx=3, pady=10 )

# titulo 
app_info =Label(frame_baixo,text='Número total de caracteres na senha',  height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
app_info.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=5, pady=1 )

# ---------------------------- Como criar um box 
var = IntVar()
var.set(8)
spin = Spinbox(frame_baixo, from_=0, to=20, width=5, textvariable=var)
spin.grid(row=2, column=0, columnspan=2, sticky=NW, padx=5, pady=8 )

# -------------------------  Caracteres ------------------------------

letra_maior = string.ascii_uppercase
letra_menor = string.ascii_lowercase
numeros = '123456789'


frame_teclado = Frame(frame_baixo, width=295, height=210, bg=cor1, pady=0, padx=0,  relief='flat')
frame_teclado.grid(row=3, column=0, sticky=NSEW, columnspan=3)

# -------------------------------- Teclado Letras maiusculas

estado1 = StringVar()
estado1.set(False)
check_1 = Checkbutton(frame_teclado, width=1, var=estado1, onvalue=letra_maior, offvalue='off', relief='flat', bg=cor1)
check_1.grid(row=0, column=0, sticky=NW, padx=2, pady=5)

app_info =Label(frame_teclado, text='ABC letras maiúsculas',  height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
app_info.grid(row=0, column=1,  sticky=NW, padx=2, pady=5)


# -------------------- Teclado Letras minusculas

estado_2 = StringVar()
estado_2.set(False)
check_2 = Checkbutton(frame_teclado, width=1, var=estado_2, onvalue=letra_menor, offvalue='off', relief='flat', bg=cor1)
check_2.grid(row=1, column=0, sticky=NW, padx=2, pady=5)

app_info =Label(frame_teclado, text='abc letras minúsculas',  height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
app_info.grid(row=1, column=1,  sticky=NW, padx=2, pady=5)

#---------------------------------- Teclado numeros

estado_3 = StringVar()
estado_3.set(False)
check_3 = Checkbutton(frame_teclado, width=1, var=estado_3, onvalue=numeros, offvalue='off', relief='flat', bg=cor1)
check_3.grid(row=2, column=0, sticky=NW, padx=2, pady=5)

app_info =Label(frame_teclado, text='123 números',  height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
app_info.grid(row=2, column=1,  sticky=NW, padx=2, pady=5)



# --------------------- Criando um  Botão 

botao_senha =Button(frame_teclado, command=criar_senha,  text='Gerar senha', width=34,  height=1,  relief='flat', overrelief='solid',  anchor='center', font=('Ivy 10 bold'), bg=cor0, fg=cor1)
botao_senha.grid(row=5, column=0,  sticky=NSEW, padx=5, pady=7, columnspan=5)

janela.mainloop()




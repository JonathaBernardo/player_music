#IMPORTAÇÕES

#Tkinter
import tkinter as tk
#Pillow
from PIL import Image, ImageTk

#cores
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co3 = "#2e2d2c"  # black
co4 = "#403d3d"   # letra
co5 = "#4a88e8"  # Azul

#Janela

janela = tk.Tk()
janela.title("")
janela.geometry('352x255')
janela.configure(background=co1)
janela.resizable(width=tk.FALSE, height=tk.FALSE)

#JANELAS

frame_esquerdo = tk.Frame(janela, width=150, height=150, bg=co3)
frame_esquerdo.grid(row=0, column=0, pady=1, padx=1, sticky=tk.NSEW)

frame_direito = tk.Frame(janela, width=250, height=150, bg=co3)
frame_direito.grid(row=0, column=1, pady=1, padx=0, sticky=tk.NSEW)

frame_baixo = tk.Frame(janela, width=404, height=100, bg=co3)
frame_baixo.grid(row=1, columnspan=3, pady=1, padx=0, sticky=tk.NSEW)

#Logo

img_1 = Image.open('icons1.png')
img_1 = img_1.resize((130,130))
img_1 = ImageTk.PhotoImage(img_1)
e_logo = tk.Label(frame_esquerdo, height=130, image=img_1, compound=tk.LEFT, padx=0, anchor='nw', font=('ivy 16 bold'), bg=co3, fg=co3)
e_logo.place(x=13, y=15)

#FUNÇÕES

with open('playlist.txt', 'r') as lista:
    linha = lista.readlines()
def play_musica():
    rodando = lista_box.get(tk.ACTIVE)
    cmd['text'] = rodando


#CONFIGURANDO JANELA DIREITA

lista_box = tk.Listbox(frame_direito, width=22, height=10, selectmode=tk.SINGLE, font=('arial 9 bold'), bg=co3, fg=co1)
lista_box.grid(row=0, column=0)

#SCROLL 1
scr = tk.Scrollbar(frame_direito)
scr.grid(row=0, column=1, sticky=tk.NSEW)

lista_box.config(yscrollcommand=scr.set)
scr.config(command=lista_box.yview())

#SCROLL 2
scr2 = tk.Scrollbar(frame_direito)
scr2.grid(row=0, column=1, sticky=tk.NSEW)

lista_box.config(yscrollcommand=scr.set)
scr.config(command=lista_box.xview())

for lista in linha:
    lista_box.insert(tk.END, lista.strip('.'))

#MENU
cmd = tk.Label(frame_baixo, text='MENU', width=44, justify=tk.LEFT, anchor='nw', font=('ivy 10 bold'), bg=co3, fg=co1)
cmd.place(x=0, y=1)

#BOTÕES

##VOLTAR
voltar = Image.open('voltar.png')
voltar = voltar.resize((30,30))
voltar = ImageTk.PhotoImage(voltar)
voltar_r = tk.Button(frame_baixo, width=40, height=40, image=voltar, font=('ivy 10'), relief=tk.RAISED, overrelief=tk.RIDGE, bg=co3, fg=co4)
voltar_r.place(x=38, y=35)

##PLAY

play = Image.open('play.png')
play = play.resize((30,30))
play = ImageTk.PhotoImage(play)
play_r = tk.Button(frame_baixo, command=play_musica,  width=40, height=40, image=play, font=('ivy 10'), relief=tk.RAISED, overrelief=tk.RIDGE, bg=co3, fg=co4)
play_r.place(x=88, y=35)

##AVANÇAR

avancar = Image.open('avancar.png')
avancar = avancar.resize((30,30))
avancar = ImageTk.PhotoImage(avancar)
avancar_r = tk.Button(frame_baixo, width=40, height=40, image=avancar, font=('ivy 10'), relief=tk.RAISED, overrelief=tk.RIDGE, bg=co3, fg=co4)
avancar_r.place(x=138, y=35)

##PAUSAR

pausar = Image.open('pausar.png')
pausar = pausar.resize((30,30))
pausar = ImageTk.PhotoImage(pausar)
pausar_r = tk.Button(frame_baixo, width=40, height=40, image=pausar, font=('ivy 10'), relief=tk.RAISED, overrelief=tk.RIDGE, bg=co3, fg=co4)
pausar_r.place(x=188, y=35)

##PARAR

parar = Image.open('parar.png')
parar = parar.resize((30,30))
parar = ImageTk.PhotoImage(parar)
parar_r = tk.Button(frame_baixo, width=40, height=40, image=parar, font=('ivy 10'), relief=tk.RAISED, overrelief=tk.RIDGE, bg=co3, fg=co4)
parar_r.place(x=238, y=35)



#TOCANDO MÚSICA



janela.mainloop()

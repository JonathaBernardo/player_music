from tkinter import *
import Editor
root = Tk()
ListBox = Listbox(root, Editar.editor())
ListBox.pack()
root.mainloop()

barra_de_menu = tk.Menu(frame_esquerdo, bg=co3, fg=co3)
menu_contatos = tk.Menu(barra_de_menu)
menu_contatos.add_command(label='Adicionar', command=semcomando)
menu_contatos.add_command(label='Editar', command=semcomando)
menu_contatos.add_command(label='Excluir', command=semcomando)
menu_contatos.add_separator()
menu_contatos.add_command(label='Fechar', command=semcomando)
janela.config(menu=barra_de_menu)

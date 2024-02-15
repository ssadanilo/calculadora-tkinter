# Importando Tkinter e ttk
from tkinter import *
from tkinter import ttk

# Cores
cor_preta = '#111212'
cor_branca = '#f5f7f7'
cor_cinza = '#d6d5d2'
cor_laranja = '#fcb308'

# Criando a janela
janela = Tk()
janela.title('Calculadora')
janela.geometry('235x310')
janela.config(bg=cor_preta)

# Criando frames
frame_tela = Frame(janela, width=235, height=50, bg=cor_preta)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=261, bg=cor_preta)
frame_corpo.grid(row=1, column=0)

# Criando variável Valores_obtidos fora da função
valores_obtidos = ''

# Criando Label
texto_tela = StringVar()

# Criando função para inserir valores
def inserir_valores(event):

    global valores_obtidos
    valores_obtidos = valores_obtidos + str(event)

    # Passando valor para a tela
    texto_tela.set(valores_obtidos)

# Criando função para calcular valores
def calcular_valores():
    global valores_obtidos
    resultado = eval(valores_obtidos)
    texto_tela.set(str(resultado))

# Criando função para limpar a tela
def limpar_tela():
    global valores_obtidos
    valores_obtidos = ''
    texto_tela.set('')

app_label = Label(frame_tela, textvariable=texto_tela, width=16, height=2, padx=7, relief='flat', anchor='e', justify='right', font=('tahoma 18'), bg=cor_preta, fg=cor_branca)
app_label.place(x=0, y=0,)

# Criando botões
button_clean = Button(frame_corpo, text='C', command= limpar_tela, width=11 ,height=2, bg=cor_cinza, font=('tahoma 13 bold'), relief=RAISED, overrelief=RIDGE)
button_clean.place(x=0 ,y=0)
button_resto = Button(frame_corpo, text='%', command= lambda: inserir_valores('%'), width=5 ,height=2, bg=cor_cinza, font=('tahoma 13 bold'), relief=RAISED, overrelief=RIDGE)
button_resto.place(x=118 ,y=0)
button_divisao = Button(frame_corpo, text='/', command= lambda: inserir_valores('/'), width=5 ,height=2, bg=cor_laranja, fg=cor_branca, font=('tahoma 13 bold'), relief=RAISED, overrelief=RIDGE)
button_divisao.place(x=177 ,y=0)

button_7 = Button(frame_corpo, text='7', command= lambda: inserir_valores('7'), width=5 ,height=2, bg=cor_cinza, font=('tahoma 13 bold'), relief=RAISED, overrelief=RIDGE)
button_7.place(x=0,y=52)
button_8 = Button(frame_corpo, text='8', command= lambda: inserir_valores('8'), width=5 ,height=2, bg=cor_cinza, font=('tahoma 13 bold'), relief=RAISED, overrelief=RIDGE)
button_8.place(x=59 ,y=52) 
button_9 = Button(frame_corpo, text='9', command= lambda: inserir_valores('9'), width=5 ,height=2, bg=cor_cinza, font=('tahoma 13 bold'), relief=RAISED, overrelief=RIDGE)
button_9.place(x=118 ,y=52)
button_multiplicacao = Button(frame_corpo, text='*',command= lambda: inserir_valores('*'), width=5 ,height=2, bg=cor_laranja, fg=cor_branca, font=('tahoma 13 bold'), relief=RAISED, overrelief=RIDGE)
button_multiplicacao.place(x=177 ,y=52)

button_4 = Button(frame_corpo, text='4', command= lambda: inserir_valores('4'), width=5 ,height=2, bg=cor_cinza, font=('tahoma 13 bold'), relief=RAISED, overrelief=RIDGE)
button_4.place(x=0,y=104)
button_5 = Button(frame_corpo, text='5', command= lambda: inserir_valores('5'), width=5 ,height=2, bg=cor_cinza, font=('tahoma 13 bold'), relief=RAISED, overrelief=RIDGE)
button_5.place(x=59 ,y=104) 
button_6 = Button(frame_corpo, text='6', command= lambda: inserir_valores('6'), width=5 ,height=2, bg=cor_cinza, font=('tahoma 13 bold'), relief=RAISED, overrelief=RIDGE)
button_6.place(x=118 ,y=104)
button_subitracao = Button(frame_corpo, text='-', command= lambda: inserir_valores('-'), width=5 ,height=2, bg=cor_laranja, fg=cor_branca, font=('tahoma 13 bold'), relief=RAISED, overrelief=RIDGE)
button_subitracao.place(x=177 ,y=104)

button_3 = Button(frame_corpo, text='1', command= lambda: inserir_valores('1'), width=5 ,height=2, bg=cor_cinza, font=('tahoma 13 bold'), relief=RAISED, overrelief=RIDGE)
button_3.place(x=0,y=156)
button_2 = Button(frame_corpo, text='2', command= lambda: inserir_valores('2'), width=5 ,height=2, bg=cor_cinza, font=('tahoma 13 bold'), relief=RAISED, overrelief=RIDGE)
button_2.place(x=59 ,y=156) 
button_1 = Button(frame_corpo, text='3', command= lambda: inserir_valores('3'), width=5 ,height=2, bg=cor_cinza, font=('tahoma 13 bold'), relief=RAISED, overrelief=RIDGE)
button_1.place(x=118 ,y=156)
button_somar = Button(frame_corpo, text='+', command= lambda: inserir_valores('+'), width=5 ,height=2, bg=cor_laranja, fg=cor_branca, font=('tahoma 13 bold'), relief=RAISED, overrelief=RIDGE)
button_somar.place(x=177 ,y=156)

button_zero = Button(frame_corpo, text='0', command= lambda: inserir_valores('0'), width=11 ,height=2, bg=cor_cinza, font=('tahoma 13 bold'), relief=RAISED, overrelief=RIDGE)
button_zero.place(x=0 ,y=208)
button_ponto = Button(frame_corpo, text='.', command= lambda: inserir_valores('.'), width=5 ,height=2, bg=cor_cinza, font=('tahoma 13 bold'), relief=RAISED, overrelief=RIDGE)
button_ponto.place(x=118 ,y=208)
button_igual = Button(frame_corpo, text='=', command= calcular_valores, width=5 ,height=2, bg=cor_laranja, fg=cor_branca, font=('tahoma 13 bold'), relief=RAISED, overrelief=RIDGE)
button_igual.place(x=177 ,y=208)


# Criando o loop ja janela para mostrar a iterface
janela.mainloop()
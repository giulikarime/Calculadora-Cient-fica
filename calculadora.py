from tkinter import *
import tkinter as tk
import math

#cores
color1 = "#191717"
color2 = "#678567"
color3 = "#3D3A3A"
color4 = "#5E5959"
color5 = "#468194"
color6 = "#6094A6"
color7 = "#F0E6E4"

#Janela

win = Tk()
win.geometry("440x560+50+50")
win.title("Calculadora")
win.iconbitmap("img/calculator_icon.ico")
win.config(bg=color1)

#Frames

TelaCal = Frame(win,height="100",bg=color1)
TelaCal.grid(row=0,column=0,padx=20,pady=20)

TecladoCal = Frame(win,width="360",height="400",bg=color1)
TecladoCal.grid(row=1,column=0,padx=18)

VersãoCal = Frame(win,width="400",height="20",bg=color1)
VersãoCal.grid(row=3,column=0,padx=20,pady=20)


#Funções

global valores

valores = ""
MostrarTela = StringVar()
Memory = "0"

labelScreen = Label(TelaCal, textvariable=MostrarTela, bg=color5, fg=color7, font=("Ivy 24 bold"),width="18",height=2,anchor="e",justify="right")
labelScreen.grid(row=0,column=0)

Versão = Label(VersãoCal,text="V.:1.2",bg=color1,fg=color7,font=("Ivy 9"))
Versão.place(x=340)

def InserirTexto(event):
    global valores

    valores = valores + str(event)
    MostrarTela.set(valores)

def Calcular():
   global valores

   modulos = ['math.tan','math.sin','math.cos','math.sqrt','math.log','math.pow']
   for i in modulos:
        if i =="math.tan":
            valores = valores.replace('tan',i)
        if i =="math.sin":
            valores = valores.replace('sin',i)
        if i =="math.cos":
            valores = valores.replace('cos',i)
        if i =="math.sqrt":
            valores = valores.replace('sqrt',i)
        if i =="math.pow":
            valores = valores.replace('pow',i)
        if i =="math.log":
            valores = valores.replace('log',i)
   
   resultado = eval(valores)
   MostrarTela.set(str(resultado))
   valores = str(resultado)


def Clean():
   global valores
   
   valores = ''
   MostrarTela.set('')

def Teclado(event):
    tecla = event.keysym
    char = event.char

    if tecla == "Return":
        Calcular()

    elif tecla == "BackSpace":
        global valores
        valores = valores[:-1]
        MostrarTela.set(valores)
    
    elif char in "0123456789+-*/().,":
        InserirTexto(char)

    elif tecla == "Escape":
        Clean()

    elif tecla == "s":
        InserirTexto("sin(")
    elif tecla == "c":
        InserirTexto("cos(")
    elif tecla == "t":
        InserirTexto("tan(")
    elif tecla == "r":
        InserirTexto("sqrt(")
    elif tecla == "l":
        InserirTexto("log(")
    elif tecla == "p":
        InserirTexto("pow(")

def MemoryPlus():
    global Memory

    atual = MostrarTela.get()

    if atual == "":
        return

    Memory = str(float(Memory) + float(atual))

def MemoryRecall():
    global valores
    valores = Memory
    MostrarTela.set(Memory)

def MemoryMinus():
    global Memory

    atual = MostrarTela.get()

    if atual == "":
        return

    Memory = str(float(Memory) - float(atual))

def MemoryClear():
    global Memory

    Memory = "0"

#Botões

#Funções M

bt28=Button(TecladoCal,width='4',height='2',bg=color1,text='MC', fg=color7, font=("Ivy 9"), relief="flat", overrelief="raised", activebackground=color3, highlightthickness=0, borderwidth=0, command=MemoryClear)
bt28.place(x=27,y=0)
bt29=Button(TecladoCal,width='4',height='2',bg=color1,text='MR', fg=color7, font=("Ivy 9"), relief="flat", overrelief="raised", activebackground=color3, highlightthickness=0, borderwidth=0, command=MemoryRecall)
bt29.place(x=115,y=0)
bt30=Button(TecladoCal,width='4',height='2',bg=color1,text='M+', fg=color7, font=("Ivy 9"), relief="flat", overrelief="raised", activebackground=color3, highlightthickness=0, borderwidth=0, command=MemoryPlus)
bt30.place(x=207,y=0)
bt31=Button(TecladoCal,width='4',height='2',bg=color1,text='M-', fg=color7, font=("Ivy 9"), relief="flat", overrelief="raised", activebackground=color3, highlightthickness=0, borderwidth=0, command=MemoryMinus)
bt31.place(x=297,y=0)
#Primeira fileira
bt1=Button(TecladoCal,width='9',height='2',bg=color3,text='sqrt', fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color7, highlightthickness=0, borderwidth=0, command= lambda: InserirTexto("sqrt("))
bt1.place(x=0,y=50)
bt2=Button(TecladoCal,width='9',height='2',bg=color3,text='sin', fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color7, highlightthickness=0, borderwidth=0,command=lambda: InserirTexto("sin("))
bt2.place(x=90,y=50)
bt3=Button(TecladoCal,width='9',height='2',bg=color3,text='cos', fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color7, highlightthickness=0, borderwidth=0,command=lambda: InserirTexto("cos("))
bt3.place(x=180,y=50)
bt4=Button(TecladoCal,width='9',height='2',bg=color3,text='tan', fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color7, highlightthickness=0, borderwidth=0,command=lambda: InserirTexto("tan("))
bt4.place(x=270,y=50)

#Segunda Fileira
bt5=Button(TecladoCal,width='9',height='2',bg=color3,text='pow', fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color7, highlightthickness=0, borderwidth=0,command=lambda: InserirTexto("pow("))
bt5.place(x=0,y=100)
bt6=Button(TecladoCal,width='9',height='2',bg=color3,text='log', fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color7, highlightthickness=0, borderwidth=0,command=lambda: InserirTexto("log("))
bt6.place(x=90,y=100)
bt7=Button(TecladoCal,width='9',height='2',bg=color3,text='(', fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color7, highlightthickness=0, borderwidth=0,command=lambda: InserirTexto("("))
bt7.place(x=180,y=100)
bt8=Button(TecladoCal,width='9',height='2',bg=color3,text=')', fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color7, highlightthickness=0, borderwidth=0,command=lambda: InserirTexto(")"))
bt8.place(x=270,y=100)

#Terceira Fileira
bt9=Button(TecladoCal,width='9',height='2',bg=color3,text='%', fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color7, highlightthickness=0, borderwidth=0,command=lambda: InserirTexto("%"))
bt9.place(x=0,y=160)
bt10=Button(TecladoCal,width='9',height='2',bg=color3,text='/', fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color7, highlightthickness=0, borderwidth=0,command=lambda: InserirTexto("/"))
bt10.place(x=90,y=160)
bt11=Button(TecladoCal,width='19',height='2',bg=color3,text='C', fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color7, highlightthickness=0, borderwidth=0,command=Clean)
bt11.place(x=180,y=160)

#Quarta Fileira
bt12=Button(TecladoCal,width='9',height='2',bg=color3,text='1', fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color7, highlightthickness=0, borderwidth=0,command= lambda: InserirTexto("1"))
bt12.place(x=0,y=210)
bt13=Button(TecladoCal,width='9',height='2',bg=color3,text='2', fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color7, highlightthickness=0, borderwidth=0,command=lambda: InserirTexto("2"))
bt13.place(x=90,y=210)
bt14=Button(TecladoCal,width='9',height='2',bg=color3,text='3', fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color7, highlightthickness=0, borderwidth=0,command=lambda: InserirTexto("3"))
bt14.place(x=180,y=210)
bt15=Button(TecladoCal,width='9',height='2',bg=color5,text='=', fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color6, activeforeground=color7, highlightthickness=0, borderwidth=0,command=Calcular)
bt15.place(x=270,y=210)

#Quinta Fileira
bt16=Button(TecladoCal,width='9',height='2',bg=color3,text='4', fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color7, highlightthickness=0, borderwidth=0,command=lambda: InserirTexto("4"))
bt16.place(x=0,y=260)
bt17=Button(TecladoCal,width='9',height='2',bg=color3,text='5', fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color7, highlightthickness=0, borderwidth=0,command=lambda: InserirTexto("5"))
bt17.place(x=90,y=260)
bt18=Button(TecladoCal,width='9',height='2',bg=color3,text='6', fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color7, highlightthickness=0, borderwidth=0,command= lambda: InserirTexto("6"))
bt18.place(x=180,y=260)
bt19=Button(TecladoCal,width='9',height='2',bg=color3,text='+', fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color7, highlightthickness=0, borderwidth=0,command=lambda: InserirTexto("+"))
bt19.place(x=270,y=260)

#Sexta Fileira
bt20=Button(TecladoCal,width='9',height='2',bg=color3,text='7', fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color7, highlightthickness=0, borderwidth=0,command=lambda: InserirTexto("7"))
bt20.place(x=0,y=310)
bt21=Button(TecladoCal,width='9',height='2',bg=color3,text='8', fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color7, highlightthickness=0, borderwidth=0,command=lambda: InserirTexto("8"))
bt21.place(x=90,y=310)
bt22=Button(TecladoCal,width='9',height='2',bg=color3,text='9', fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color7, highlightthickness=0, borderwidth=0,command=lambda: InserirTexto("9"))
bt22.place(x=180,y=310)
bt23=Button(TecladoCal,width='9',height='2',bg=color3,text='-', fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color7, highlightthickness=0, borderwidth=0,command=lambda: InserirTexto("-"))
bt23.place(x=270,y=310)

#Sétima Fileira
bt24=Button(TecladoCal,width='9',height='2',bg=color3,text=',', fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color7, highlightthickness=0, borderwidth=0,command=lambda: InserirTexto(","))
bt24.place(x=0,y=360)
bt25=Button(TecladoCal,width='9',height='2',bg=color3,text='0', fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color7, highlightthickness=0, borderwidth=0,command=lambda: InserirTexto("0"))
bt25.place(x=90,y=360)
bt26=Button(TecladoCal,width='9',height='2',bg=color3,text='.', fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color7, highlightthickness=0, borderwidth=0,command=lambda: InserirTexto("."))
bt26.place(x=180,y=360)
bt27=Button(TecladoCal,width='9',height='2',bg=color3,text='x', fg=color7, font=("Ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color7, highlightthickness=0, borderwidth=0,command=lambda: InserirTexto("x"))
bt27.place(x=270,y=360)

win.bind("<Key>",Teclado)
win.mainloop()
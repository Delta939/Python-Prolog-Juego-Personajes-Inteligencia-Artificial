import tkinter as tk
from tkinter import messagebox
from pyswip import *

root= tk.Tk() # create window
prolog=Prolog()

canvas1 = tk.Canvas(root, width = 450, height = 450)
canvas1.configure(bg="yellow")
canvas1.pack()
button3 = tk.Button (root, text="Inteligencia Artificial UACM",bg="cyan")
canvas1.create_window(250, 10, window=button3)
button3.config(state='disabled')

def clicked():
    var = tk.StringVar()
    MsgBox1 = tk.messagebox.askquestion ('Simpson','Tu personaje usa patineta')
    if MsgBox1 == 'yes':
        v1="patineta"
        print(v1)
        #root.destroy()
        MsgBox2 = tk.messagebox.askquestion ('Simpson','Tu personaje usa resortera')
        if MsgBox2 == 'yes':
            v2="resortera"
            print(v2)
            #root.destroy()
        MsgBox3 = tk.messagebox.askquestion ('Simpson','Tu personaje hace bromas')
        if MsgBox3 == 'yes':
            v3="bromas"
            print(v3)
            #root.destroy()
            
        prolog.consult("padre.pl")
        q="familia("+v1+","+v2+","+v3+",X)."       
        for r in prolog.query(q):
            print (r["X"],"Simpson")
            var.set(r["X"])
            #tk.Label(canvas1,text="", fg="black",textvariable=var.get(),bg="White").place(x=250,y=30)  
            button2 = tk.Button (root, text="Tu personaje es "+var.get(),bg="cyan", command=clicked)
            canvas1.create_window(250, 360, window=button2)
            button2.config(state='disabled')
            
            
            if r["X"] == "bart":
                    img = tk.PhotoImage(file="bart.png")
                    fondo = tk.Label(canvas1, image=img,bg="yellow").place(x=150,y=90)
                    

            
    elif MsgBox1 == 'no':
        tk.messagebox.showinfo('Simpson','Regreso al menu')

    MsgBox4 = tk.messagebox.askquestion ('Simpson','Tu personaje toca el saxofon')
    if MsgBox4 == 'yes':
        v1="saxofon"
        print(v1)
        #root.destroy()
        MsgBox5 = tk.messagebox.askquestion ('Simpson','Tu personaje lee libros')
        if MsgBox5 == 'yes':
            v2="libros"
            print(v2)
            #root.destroy()
        MsgBox6 = tk.messagebox.askquestion ('Simpson','Tu personaje es inteligente')
        if MsgBox6 == 'yes':
            v3="inteligente"
            print(v3)
            #root.destroy()
            
        prolog.consult("padre.pl")
        q="familia("+v1+","+v2+","+v3+",X)."       
        for r in prolog.query(q):
            print (r["X"],"Simpson")
            var.set(r["X"])
            #tk.Label(canvas1,text="", fg="black",textvariable=var.get(),bg="White").place(x=250,y=30)  
            button2 = tk.Button (root, text="Tu personaje es "+var.get(),bg="cyan", command=clicked)
            canvas1.create_window(250, 360, window=button2)
            button2.config(state='disabled')
            
            
            if r["X"] == "lisa":
                    img = tk.PhotoImage(file="lisa.png")
                    fondo = tk.Label(canvas1, image=img,bg="yellow").place(x=150,y=90)
                           
            
    elif MsgBox4 == 'no':
        tk.messagebox.showinfo('Simpson','Regreso al menu')

    MsgBox7 = tk.messagebox.askquestion ('Simpson','Tu personaje come rosquillas')
    if MsgBox7 == 'yes':
        v1="rosquillas"
        print(v1)
        #root.destroy()
        MsgBox8 = tk.messagebox.askquestion ('Simpson','Tu personaje toma cerveza')
        if MsgBox8 == 'yes':
            v2="cerveza"
            print(v2)
            #root.destroy()
        MsgBox9 = tk.messagebox.askquestion ('Simpson','Tu personaje trabaja en la planta nuclear')
        if MsgBox9 == 'yes':
            v3="nuclear"
            print(v3)
            #root.destroy()
            
        prolog.consult("padre.pl")
        q="familia("+v1+","+v2+","+v3+",X)."       
        for r in prolog.query(q):
            print (r["X"],"Simpson")
            var.set(r["X"])
            #tk.Label(canvas1,text="", fg="black",textvariable=var.get(),bg="White").place(x=250,y=30)  
            button2 = tk.Button (root, text="Tu personaje es "+var.get(),bg="cyan", command=clicked)
            canvas1.create_window(250, 360, window=button2)
            button2.config(state='disabled')
            
            
            if r["X"] == "homero":
                    img = tk.PhotoImage(file="homero.png")
                    fondo = tk.Label(canvas1, image=img,bg="yellow").place(x=150,y=90)
                             
            
    elif MsgBox7 == 'no':
        tk.messagebox.showinfo('Simpson','Regreso al menu')

    MsgBox10 = tk.messagebox.askquestion ('Simpson','Tu personaje tiene el cabello alto')
    if MsgBox10 == 'yes':
        v1="cabelloalto"
        print(v1)
        #root.destroy()
        MsgBox11 = tk.messagebox.askquestion ('Simpson','Tu personaje usa vestido verde')
        if MsgBox11 == 'yes':
            v2="vestidoverde"
            print(v2)
            #root.destroy()
        MsgBox12 = tk.messagebox.askquestion ('Simpson','Tu personaje tiene collar rojo')
        if MsgBox12 == 'yes':
            v3="collarrojo"
            print(v3)
            #root.destroy()
            
        prolog.consult("padre.pl")
        q="familia("+v1+","+v2+","+v3+",X)."       
        for r in prolog.query(q):
            print (r["X"],"Simpson")
            var.set(r["X"])
            #tk.Label(canvas1,text="", fg="black",textvariable=var.get(),bg="White").place(x=250,y=30)  
            button2 = tk.Button (root, text="Tu personaje es "+var.get(),bg="cyan", command=clicked)
            canvas1.create_window(250, 360, window=button2)
            button2.config(state='disabled')
            
            
            if r["X"] == "marge":
                    img = tk.PhotoImage(file="marge.png")
                    fondo = tk.Label(canvas1, image=img,bg="yellow").place(x=150,y=90)
                             
            
    elif MsgBox10 == 'no':
        tk.messagebox.showinfo('Simpson','Regreso al menu')


    MsgBox13 = tk.messagebox.askquestion ('Simpson','Tu personaje tiene un chupon rojo')
    if MsgBox13 == 'yes':
        v1="chuponrojo"
        print(v1)
        #root.destroy()
        MsgBox14 = tk.messagebox.askquestion ('Simpson','Tu personaje tiene un moño azul')
        if MsgBox14 == 'yes':
            v2="monoazul"
            print(v2)
            #root.destroy()
        MsgBox15 = tk.messagebox.askquestion ('Simpson','Tu personaje usa mameluco azul')
        if MsgBox15 == 'yes':
            v3="mamelucoazul"
            print(v3)
            #root.destroy()
            
        prolog.consult("padre.pl")
        q="familia("+v1+","+v2+","+v3+",X)."       
        for r in prolog.query(q):
            print (r["X"],"Simpson")
            var.set(r["X"])
            #tk.Label(canvas1,text="", fg="black",textvariable=var.get(),bg="White").place(x=250,y=30)  
            button2 = tk.Button (root, text="Tu personaje es "+var.get(),bg="cyan", command=clicked)
            canvas1.create_window(250, 360, window=button2)
            button2.config(state='disabled')
            
            
            if r["X"] == "maggie":
                    img = tk.PhotoImage(file="maggie.gif")
                    fondo = tk.Label(canvas1, image=img,bg="yellow").place(x=150,y=90)
            
    elif MsgBox13 == 'no':
        tk.messagebox.showinfo('Simpson','Regreso al menu')
        canvas1.delete("all")
        button3 = tk.Button (root, text="Inteligencia Artificial UACM",bg="cyan")
        canvas1.create_window(250, 10, window=button3)
        button3.config(state='disabled')
        button1 = tk.Button (root, text='Presiona para iniciar',bg="cyan", command=clicked)
        canvas1.create_window(250, 70, window=button1)

        img = tk.PhotoImage(file="lossimpson.png")
        fondo = tk.Label(canvas1, image=img,bg="yellow").place(x=150,y=90)  
        
        
    MsgBox16 = tk.messagebox.askquestion ('Simpson','Quieres salir')
        
    if MsgBox16 == 'yes':
        root.destroy() 
     
    elif MsgBox16 == 'no': 
     #tk.messagebox.showinfo('Simpson','Regreso al menu')
     img = tk.PhotoImage(file="lossimpson.png")
     fondo = tk.Label(canvas1, image=img,bg="yellow").place(x=150,y=90)  
        
button1 = tk.Button (root, text='Presiona para iniciar',bg="cyan", command=clicked)
canvas1.create_window(250, 70, window=button1)

img = tk.PhotoImage(file="lossimpson.png")
fondo = tk.Label(canvas1, image=img,bg="yellow").place(x=150,y=90)  
root.mainloop()

from select import select
import tkinter as tk                
from tkinter import Button, Entry, IntVar, Label, Radiobutton, StringVar, Tk, font  as tkfont 
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import *

import random
from random import choice
from traceback import print_list

class Halaman0(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Times New Roman', size=25, weight="bold", slant="roman")

        # Menggunakan container Sebagai Penampung frame

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Beranda, Halaman1, Halaman2):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # diletakan dilokasi yg sama
            # disusun
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Beranda")

    def show_frame(self, page_name):
        ''' Menggunakan Frame Sebagai halaman'''
        frame = self.frames[page_name]
        frame.tkraise()


class Beranda(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=" Pola Olahraga di Massa Pandemi Covid-19", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Penguatan Otot",
                            command=lambda: controller.show_frame("Halaman1"))
        button2 = tk.Button(self, text="Cardio",
                            command=lambda: controller.show_frame("Halaman2"))
        button1.pack()
        button2.pack()


class Halaman1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='Orange')
        self.controller = controller
        label = tk.Label(self, text="Penguatan", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Kembali Ke Beranda",
        command=lambda: controller.show_frame("Beranda"))
        button.pack(pady=10)

        Dada_list = ['Gerakan Push Up 15 Rep 2 Sets ,  Chestfly 11 Rep 2 Sets' ]
        def Dada_one():
            Dada_press = random.choice(Dada_list)
            print_list(Dada_list)
            Dada_press_label = Label(self, text = Dada_press).pack()

        Dada_button=tk.Button(self, text='Dada', command=Dada_one,).pack()

        Punggung_list = ['Gerakan Wide Pull up 10 Rep 2 Sets , Wide Push Up 15 Rep 3 Sets']
        def Punggung_one():
            Punggung_back = random.choice(Punggung_list)
            print(Punggung_list)
            Punggung_label = Label(self, text = Punggung_back).pack()

        Punggung_button=tk.Button(self, text='Punggung', command=Punggung_one,).pack()

        Pundak_list = ['Gerakan Normal Pullup 10 Rep 2 Sets, Shoulder press 13 Rep 4 Sets']
        def Pundak_one():
            Pundak_press = random.choice(Pundak_list)
            print(Pundak_list)
            Pundak_press_label = Label(self, text = Pundak_press).pack()

        Pundak_button=tk.Button(self, text='Pundak', command=Pundak_one,).pack()
        
        Lengan_list = ['Gerakan Diamond Push up 20 Rep 2 Sets, Barbell 5 kg 12 Rep 3 Sets ']
        def Lengan_one():
            Lengan_press = random.choice(Lengan_list)
            print(Lengan_list)
            Lengan_press_label = Label(self, text = Lengan_press).pack()

        Lengan_button=tk.Button(self, text='Lengan', command=Lengan_one,).pack()


class Halaman2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='orange')
        self.controller = controller
        label = tk.Label(self, text="Cardio", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Kembali Ke Beranda",
                           command=lambda: controller.show_frame("Beranda"))
        button.pack()

        Cardio_indoor_list = ['Lompat Tali , Treadmil , Naik Turun Tangga']
        def Cardio_indoor_two():
            Cardio_in = random.choice(Cardio_indoor_list)
            print(Cardio_indoor_list)
            Cardio_in_label = Label(self, text = Cardio_in).pack()

        Cardio_Indoor_button=tk.Button(self, text='Cardio Dalam Ruangan', command=Cardio_indoor_two,).pack()

        Cardio_outdoor_list = ['Lari, Jogging, Renang']
        def Cardio_outdoor_two():
            Carido_out = (Cardio_outdoor_list)
            print(Cardio_outdoor_list)
            Cardio_out_label = Label(self, text = Carido_out).pack()
 
        Cardio_outdoor_button=tk.Button(self, text='Cardio di Luar Ruangan', command=Cardio_outdoor_two,).pack()

def submit():
 perkenalan=""
 if len(stringnama.get()) == 0:
  messagebox.showerror("Error","BELUM MENGISI NAMA")
  return
 if radio.get()== 0:
  messagebox.showerror("Error","SILAHKAN MENGISI KONDISI DAHULU !!!")
  return
 elif radio.get() == 1:
  perkenalan="Fit "
 elif radio.get() == 2:
  perkenalan="Tidak Fit "

 pesan = " TETAP JAGA KESEHATAN , SAYA " +  stringnama.get() + " Kondisi Saya Sekarang Sedang " + perkenalan
 messagebox.showinfo("Greeting", pesan)
 
top = Tk() 
top.geometry("300x200")
top.title(" CHECK KONDISI KESEHATAN SEBELUM OLAHRAGA")

#creating Label 
lbnama = Label(top, text = "Nama\t:").place(x = 30,y = 10) 
lbjk = Label(text = "Kondisi Sekarang\t:").place(x = 10, y=40)


#create input 
stringnama = StringVar()
inama = Entry(top,width = 20, textvariable=stringnama).place(x = 
110, y = 10) 

#create radio
radio = IntVar()
R1 = Radiobutton(top, text="Fit", variable=radio, 
value=1).place(x=105, y=40) 
R2 = Radiobutton(top, text="Tidak Fit", variable=radio, 
value=2).place(x=105, y=60)  

#create button
btn1 = Button(top, command = submit, 
text="SUBMIT").place(x=120,y=150)
top.mainloop()


if __name__ == "__main__":
    app = Halaman0()
    app.mainloop()
from tkinter import *
import random
from tkinter import messagebox
​
renkler=["Red","Yellow","Blue","Purple","Green","Black","White","Pink","Gray","Orange","Brown"]
​
skor=0
kalansure=60
​
def basla(event):
    if kalansure==60:
        say()
    yenirenk()
def yenirenk():
    global kalansure,skor
    if kalansure>0:
        giris.focus_set()
        if giris.get().lower()==renkler[1].lower():
            skor+=1
        giris.delete(0,END)
        random.shuffle(renkler)
        etiket.config(fg=str(renkler[1]),text=str(renkler[0]))
        ekranskor.config(text="Skor:"+str(skor))
def say():
    global kalansure
    if kalansure>0:
        kalansure-=1
        ekransure.config(text="Kalan süre:"+str(kalansure))
        ekransure.after(1000,say)
    elif kalansure==0:
        messagebox.showwarning("sonuç ekranı","Süre bitti, yaptığınız skor:"+str(skor))
        
        
        
​
​
pencere=Tk()
pencere.geometry("350x350+75+75")
pencere.title("renk oyunu")
​
ekranskor=Label(pencere,text="başlamak için enter bas")
ekranskor.pack()
​
ekransure=Label(pencere,text="Kalan süre:"+str(kalansure))
ekransure.pack()
​
etiket=Label(pencere,font=("Calibri",50,"bold"))
etiket.pack()
​
giris=Entry(pencere)
pencere.bind('<Return>',basla)
giris.pack()
giris.focus_set()
​
​
mainloop()
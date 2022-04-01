import tkinter
from tkinter import *
import time
import datetime
import winsound

def alarm(ustaw_czas_alarmu):
    while True:
        time.sleep(1)
        czas = datetime.datetime.now()
        aktualny_czas = czas.strftime("%H:%M:%S")
        print('Aktualny czas: ' + str (aktualny_czas), "," 'Czas alarmu: ', ustaw_czas_alarmu)
        if aktualny_czas == ustaw_czas_alarmu:
            winsound.PlaySound("Music.wav",winsound.SND_ASYNC)
            print("Alarm!!!")
            break
 
def pobierz_czas_alarmu():
    ustaw = f"{godz.get()}:{min.get()}:{sek.get()}"
    alarm(ustaw)

def wyswietlanie():
    obecna = datetime.datetime.now().strftime("%H:%M:%S")
    l2.config(text = obecna)
    l2.after(200, wyswietlanie)
        
root = tkinter.Tk()
root.title("Alarm Michała")
root.geometry('340x200')
root.resizable(width=False,height=False)

godz = StringVar()
min = StringVar()
sek = StringVar()

l = tkinter.Label(root, text = 'Aktualna godzina: ', font = ('Calibri', 12), width = '20')
l.pack()
l2 = tkinter.Label(root, text = wyswietlanie, font=('Calibri', 25) ,bg = 'black', fg = 'green', height = '1', width = '10')
l2.place(x = 80, y = 25)
l3 = tkinter.Label(root, text = 'Godzina alarmu: \n godz. min. sek.', font = ('Calibri', 8), width = '12')
l3.place(x = 10 , y = 81)
l4 = tkinter.Label(root, text = 'Podaj wszystkie wartości (format 24 godz.)', font = ('Calibri', 8), width = '40')
l4.place(x = 48, y = 115)

egodziny = tkinter.Entry(root, textvariable = godz, bg = 'white', fg = 'black', font = 15, width = 4)
egodziny.place(x = 97, y = 85) 
eminuty = tkinter.Entry(root, textvariable = min, bg = 'white', fg = 'black', font = 15, width = 4)
eminuty.place(x = 147, y = 85)
esekundy = tkinter.Entry(root, textvariable = sek, bg = 'white', fg = 'black', font = 15, width = 4)
esekundy.place(x = 197, y = 85)

b = tkinter.Button(root, command = pobierz_czas_alarmu, text = 'Utaw alarm', font = ('Calibri', 16), bg = 'grey', fg = 'white')
b.place(x = 110, y = 140)

wyswietlanie()
root.mainloop()
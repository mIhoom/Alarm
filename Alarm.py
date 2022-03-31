import tkinter
from tkinter import *
import time
import datetime
import winsound

def wyswietlanie():
    godz1 =''
    obecna = time.strftime('%H:%M:%S')
    if obecna != godz1:
            godz1 = obecna
            l2.config(text = obecna)
    l2.after(200, wyswietlanie)

def alarm():
    while True:
        ustaw_czas_alarmu = f"{godz.get()}:{min.get()}:{sek.get()}"
        time.sleep(1)
        obecny_czas = datetime.datetime.now().strftime("%H:%M:%S")
        print("Aktualny czas: ", obecny_czas, "Czas alarmu: ", ustaw_czas_alarmu)
        if obecny_czas == ustaw_czas_alarmu:
            print("JUŻ CZAS!!!")
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        break

root = tkinter.Tk()
root.title("Alarm Michała")
root.geometry('340x200')

godz = StringVar()
min = StringVar()
sek = StringVar()

l = tkinter.Label(root, text = 'Aktualna godzina: ', font = ('Calibri', 12), width = '20')
l.pack()
l2 = tkinter.Label(root, text = wyswietlanie, font=('Calibri', 25) ,bg = 'black', fg = 'green', height = '1', width = '10')
l2.place(x = 83, y = 30)
l3 = tkinter.Label(root, text = 'Godzina alarmu: \n godz. min. sek.', font = ('Calibri', 8), width = '12')
l3.place(x = 10 , y = 96)

egodziny = tkinter.Entry(root, textvariable = godz, bg = 'white', fg = 'black', font = 15, width = 4)
egodziny.place(x = 97, y = 100) 
eminuty = tkinter.Entry(root, textvariable = min, bg = 'white', fg = 'black', font = 15, width = 4)
eminuty.place(x = 147, y = 100)
esekundy = tkinter.Entry(root, textvariable = sek, bg = 'white', fg = 'black', font = 15, width = 4)
esekundy.place(x = 197, y = 100)

b = tkinter.Button(root, command = alarm, text = 'ustaw alarm', font = ('Calibri', 16), bg = 'grey', fg = 'white')
b.place(x = 110, y = 140)

wyswietlanie()
alarm()
root.mainloop()
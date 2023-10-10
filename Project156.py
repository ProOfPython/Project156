from tkinter import *
from PIL import ImageTk, Image
from random import randint

root = Tk()
root.title('Pokemon Cards')        
root.geometry('400x400')
root.configure(background = 'snow')

def getImg(name):
    return ImageTk.PhotoImage(Image.open(name))

monInfo = {
    'Abra': 30,
    'Kadabra': 60,
    'Alakazam': 80,
    'Nidoran': 60,
    'Nidorino': 90,
    'Nidoking': 150,
    'Paras': 70,
    'Parasect': 60
}

cards = []
for i in list(monInfo.keys()):
    cards.append(getImg(f'Project156+/{ i }.jpg'))

lblP1 = Label(root, text = 'Player 1:', bg = 'light blue')
lblP1.place(relx = 0.1, rely = 0.4, anchor = CENTER)
lblP1Score = Label(root, text = 'Score:', bg = 'light blue')
lblP1Score.place(relx = 0.1, rely = 0.5, anchor = CENTER)

lblP2 = Label(root, text = 'Player 2:', bg = 'light blue')
lblP2.place(relx = 0.9, rely = 0.4, anchor = CENTER)
lblP2Score = Label(root, text = 'Score:', bg = 'light blue')
lblP2Score.place(relx = 0.9, rely = 0.5, anchor = CENTER)

lblCard = Label(root, text = '', bg = 'light blue')
lblCard.place(relx = 0.5, rely = 0.5, anchor = CENTER)

p1Score = 0
p2Score = 0

def P1Play():
    global p1Score
    monNum = randint(0, len(monInfo) - 1)
    mons = list(monInfo.keys())
    p1Score += monInfo[mons[monNum]]
    
    lblP1Score['text'] = p1Score
    lblCard['image'] = cards[monNum]

def P2Play():
    global p2Score
    monNum = randint(0, len(monInfo) - 1)
    mons = list(monInfo.keys())
    p2Score += monInfo[mons[monNum]]
    
    lblP2Score['text'] = p2Score
    lblCard['image'] = cards[monNum]

btnP1Play = Button(root, text = 'Play Move', command = lambda: P1Play())
btnP1Play.place(relx = 0.1, rely = 0.6, anchor = CENTER)
btnP2Play = Button(root, text = 'Play Move', command = lambda: P2Play())
btnP2Play.place(relx = 0.9, rely = 0.6, anchor = CENTER)

root.mainloop()
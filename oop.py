import tkinter as tk
from PIL import Image, ImageTk
import random

class Bubble:
    def __init__(self, radius, x, y, canvas):
        self.canvas=canvas
        self.oval=ImageTk.PhotoImage(Image.open("bubbl.png").resize((radius, radius)))
        self.id=canvas.create_image(x, y, image=self.oval)
        self.ran=random.randint(5, 7)
    def move(self):
        self.canvas.move(self.id, 0, -self.ran)
        if self.canvas.coords(self.id) and self.canvas.coords(self.id)[1]<-20:
            self.canvas.delete(self.id)
class Starfish:
    def __init__(self, x, y, canvas):
        self.canvas=canvas
        self.star=ImageTk.PhotoImage(Image.open("starfish.png").resize((100, 100)))
        self.id=canvas.create_image(x, y, image=self.star)
        self.direction=1
        self.ran=2
    def move(self):
        self.canvas.move(self.id, self.ran * self.direction, 0)
        if self.canvas.coords(self.id)[0]>self.canvas.winfo_width() or self.canvas.coords(self.id)[0]<0:
            self.direction*=-1

class Fish:
    def __init__(self, x, y, canvas):
        self.canvas=canvas
        self.fish=ImageTk.PhotoImage(Image.open("fish.png").resize((100, 100)))
        self.id=canvas.create_image(x, y, image=self.fish)
        self.direction=1
        self.ran=3
    def move(self):
        self.canvas.move(self.id, self.ran * self.direction, 0)
        if self.canvas.coords(self.id)[0]>self.canvas.winfo_width() or self.canvas.coords(self.id)[0]<0:
            self.direction*=-1
class Pufferfish:
    def __init__(self, x, y, canvas):
        self.canvas=canvas
        self.pufferfish=ImageTk.PhotoImage(Image.open("2fish.png").resize((80, 80)))
        self.id=canvas.create_image(x, y, image=self.pufferfish)
        self.direction=1
        self.ran=4
    def move(self):
        self.canvas.move(self.id, self.ran * self.direction, 0)
        if self.canvas.coords(self.id)[0]>self.canvas.winfo_width() or self.canvas.coords(self.id)[0]<0:
            self.direction*=-1
class Shark:
    def __init__(self, x, y, canvas):
        self.canvas=canvas
        self.shark=ImageTk.PhotoImage(Image.open("shark.png").resize((200, 200)))
        self.id=canvas.create_image(x, y, image=self.shark)
        self.direction=1
        self.ran=2
    def move(self):
        self.canvas.move(self.id, self.ran * self.direction, 0)
        if self.canvas.coords(self.id)[0]>self.canvas.winfo_width() or self.canvas.coords(self.id)[0]<0:
            self.direction*=-1

def main():
    win = tk.Tk()
    canvas = tk.Canvas(win, width=800, height=800, bg="#70dee1")
    canvas.pack()

    list_bubble=[]


    star=Starfish(100, 300, canvas)
    fish=Fish(450, 500, canvas)
    pufferfish=Pufferfish(450, 200, canvas)
    shark=Shark(100, 700, canvas)
    def anim():
        if random.randint(1, 10)==1:
            list_bubble.append(Bubble(random.randint(20, 50), random.randint(20, 700), 600, canvas))
        for bubble in list_bubble:
            bubble.move()
        star.move()
        fish.move()
        pufferfish.move()
        shark.move()
        win.after(10, anim)
    anim()

    win.mainloop()
if __name__=="__main__":
    main()


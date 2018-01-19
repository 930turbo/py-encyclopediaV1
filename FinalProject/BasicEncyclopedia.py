import tkinter
import tkinter as tk
from tkinter import *
import pygame as pg

pg.init()
DESCRIPTIONS = ("Subaru info", "BMW info", "Nissan info", "Mercedes info", "Honda info", "Mazda info")

class StartScreen:
    def __init__(self, master):

        text_list = '''Welcome to Gianni's Encyclopedia of Cars!

        This is a collection of information regarding cars
        which I have put together for your convenience. The only
        real reason you would be interested in this would be
        if you wish to find out more about certain mechanical
        parts from different cars. Feel free to contribute!

        If you enjoy the application, kindly send feedback to
        giancarlo@northboropcs.com
        ________________________________________
         EXIT THIS WINDOW TO BEGIN APPLICATION!
        '''.split('\n')

        class StartMenu:
            def __init__(self, screen_rect, lst):
                self.srect = screen_rect
                self.lst = lst
                self.size = 30
                self.color = (255, 0, 0)
                self.buff_centery = self.srect.height / 2 + 5
                self.buff_lines = 50
                self.timer = 0.0
                self.delay = 0
                self.make_surfaces()

            def make_text(self, message):
                font = pg.font.SysFont('Caslon', self.size)
                text = font.render(message, True, self.color)
                rect = text.get_rect(center=(self.srect.centerx, self.srect.centery + self.buff_centery))
                return text, rect

            def make_surfaces(self):
                self.text = []
                for i, line in enumerate(self.lst):
                    l = self.make_text(line)
                    l[1].y += i * self.buff_lines
                    self.text.append(l)

            def update(self):
                if pg.time.get_ticks() - self.timer > self.delay:
                    self.timer = pg.time.get_ticks()
                    for text, rect in self.text:
                        rect.y -= 1

            def render(self, surf):
                for text, rect in self.text:
                    surf.blit(text, rect)

        screen = pg.display.set_mode((800, 600))
        screen_rect = screen.get_rect()
        clock = pg.time.Clock()
        done = False
        cred = StartMenu(screen_rect, text_list)

        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
            screen.fill((0, 0, 0))
            cred.update()
            cred.render(screen)
            pg.display.update()
            clock.tick(60)

        pg.quit()
        self.master = master

        self.button1 = tk.Button(self.master, text = 'Giannis Car Encyclopedia\nClick the screen to enter', width = 100, height = 50, command = self.new_window)
        self.button1.pack()

    def new_window(self):
        self.app = BookScreen(self.master)

class infoScreen:
    def __init__(self, value, name):
        top = Tk()
        top.title(name)
        top.resizable(0, 0)
        T = Text(top, height=2, width=30)
        T.pack()
        T.insert(END, DESCRIPTIONS[value])
        T.configure(state='disabled')

class BookScreen:
    def __init__(self, master):

        def immediately(e):
            index = Lb1.curselection()[0]
            infoScreen(index, Lb1.get(index))
            print(Lb1.get(index))
            Lb1.curselection()

        top = Tk()
        top.resizable(0,0)
        Lb1 = Listbox(top)
        Lb1.insert(1, "Subaru")
        Lb1.insert(2, "BMW")
        Lb1.insert(3, "Nissan")
        Lb1.insert(4, "Mercedes")
        Lb1.insert(5, "Honda")
        Lb1.insert(6, "Mazda")

        Lb1.pack()

        Lb1.bind('<<ListboxSelect>>', immediately)
        top.mainloop()
        def close_windows(self):
            self.master.destroy()

def main():
    root = tk.Tk()
    app = StartScreen(root)
    root.mainloop()

if __name__ == '__main__':
    main()
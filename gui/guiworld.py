#!/usr/bin/env python3
# -*- coding: utf8 -*-
'template style'

from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()

        self.alterButton = Button(self, text='hello', command=self.hello)
        self.alterButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello %s' % name)



app = Application()

app.master.title('Hello world')

app.mainloop()
import tkinter as tk


class Button:
    def __init__(self,ui,uiclass, text,page):
        self.uiclass = uiclass
        self.ui = ui
        self.text = text
        self.page = page
        self.build()
    
    def build(self):
        self.btn = tk.Button(self.ui, text=self.text,font=("Arial", 12, "bold"),width=40,command=self.pressed)
        self.btn.pack(pady=5)
    
    def hide(self):
        self.btn.pack_forget()
    
    def pressed(self):
        self.uiclass.load_page(self.text)
        


class Title:
    def __init__(self,ui,text):
        self.ui = ui
        self.text = text
        self.title = tk.Label(self.ui, text=self.text)

    def build(self):
        self.title.pack(pady=20)

    def hide(self):
        self.title.pack_forget()

class Label:
    def __init__(self,ui,text):
        self.ui = ui
        self.text = text
        self.label =tk.Label(self.ui, text=self.text)

    def build(self):
        self.label.pack(pady=20,side=tk.BOTTOM)

    def hide(self):
        self.label.pack_forget()

class Menu:
    def __init__(self,uiclass,ui,opts,pages):
        # Inherit functions from UI

        self.uiclass = uiclass
        self.ui = ui
    
        self.options = opts
        self.buttons = []
        self.pages = pages

    def build(self):
        for i,option in enumerate(self.options):
            self.buttons.append(Button(self.ui,self.uiclass,option[0],self.pages[i]))
            

    def hide(self):
        for button in self.buttons:
            button.hide()



class Canvas:
    def __init__(self):
        pass

class Icon:
    def __init__(self,ui,icon):
        self.ui = ui
        self.icon = icon

    def build(self):
        icon = tk.PhotoImage(file=self.icon)
        self.ui.iconphoto(False, icon)

    def hide(self):
        pass
    

class Entry:
    def __init__(self,ui):
        self.ui = ui

    def build(self):
        self.entry = tk.Entry(self.ui)
        self.entry.pack(pady=10)

    def hide(self):
        self.entry.pack_forget()
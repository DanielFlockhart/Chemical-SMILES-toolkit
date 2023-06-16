

import tkinter as tk
from tkinter import ttk
import os
import sys
from ui.pages import *
sys.path.insert(0, os.path.abspath('..'))
from utils import *

from ui.styles import *
from ui.controller import UIController
class UI:
    def __init__(self,options):
        self.ui = tk.Tk()
        self.controller = UIController(self.ui)
        self.ui.config(bg=colour_codes["background"])
        self.docs_folder = os.path.join(get_directory(),"docs")
        self.icon = os.path.join(self.docs_folder,r"images\benzene.png")
        self.build_ui(options)
        self.pages = [Page("Menu",self.ui),Page("Choice1",self.ui)]
        
        

    def build_ui(self,opts):
        self.ui.geometry("500x500")
    
        self.ui.title("Chemical Smiles Toolkit")
        
        self.title = Title(self.ui,"Chemical Smiles Toolkit")
        self.buttons = self.build_buttons(opts)
        self.icon = self.build_icon()
        self.new_label = Label(self.ui,"Created by Daniel Flockhart 16/06/2023")

    
    def build_buttons(self,options):
        buttons = []
        for i,option in enumerate(options):
            buttons.append(Button(self.ui,text=option[0],command=option[1]))
            
        return buttons
    

    def build_icon(self):
        # Set icon
        icon = tk.PhotoImage(file=self.icon)
        self.ui.iconphoto(False, icon)
        return icon

    def exit_program(self):
        self.ui.destroy()

    def start_program(self):
        self.ui.mainloop()


class Button:
    def __init__(self,ui, text,command):
        self.ui = ui
        self.text = text
        self.build_btn()
        
    
    def build_btn(self):
        self.ui.style = create_button_style()
        self.btn = ttk.Button(self.ui, text=self.text,width=50,style="Button.TButton")
        self.btn.pack(pady=5)



class Title:
    def __init__(self,ui,text):
        self.ui = ui
        self.text = text
        self.build_title()

    def build_title(self):
        self.ui.style = create_title_style()
        self.title = ttk.Label(self.ui, text=self.text, style="Title.TLabel")
        self.title.pack(pady=20)

class Label:
    def __init__(self,ui,text):
        self.ui = ui
        self.text = text
        self.build_label()

    def build_label(self):
        self.ui.style = create_label_style()
        self.label = ttk.Label(self.ui, text=self.text, style="Label.TLabel")
        self.label.pack(pady=20,side=tk.BOTTOM) # Temp

class Menu:
    def __init__(self,ui,opts):
        self.ui = ui
        self.options = opts
        self.build_menu()

    def build_menu(self):
        pass



class Canvas:
    def __init__(self):
        pass
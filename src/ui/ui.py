
import tkinter as tk
import os
import sys

sys.path.insert(0, os.path.abspath('..'))
from utils import *
from ui.pages import *
from ui.styles import *
from ui.widgets import *


class UI:
    def __init__(self,options,size=(500,500)):
        self.size = size
        self.ui = tk.Tk()
        self.docs_folder = os.path.join(get_directory(),"docs")
        self.title_text = "Chemical Smiles Toolkit"
        self.build_ui()
        self.build_pages(options)
        
        
        

    def build_ui(self):
        self.ui.geometry(f"{self.size[0]}x{self.size[1]}")
        self.ui.title(self.title_text)
        self.persisent_widgets = [Icon(self.ui,os.path.join(self.docs_folder,r"images\benzene.png")),
                                  tk.Button(self.ui,text="Menu",command=self.restart_program).pack(side=tk.BOTTOM),
                                  Label(self.ui,"Created by Daniel Flockhart 16/06/2023")]
        self.ui.geometry(f"{self.size[0]}x{self.size[1]}")
        self.ui.title(self.title_text)
        
    def build_pages(self,options):
        
        self.pages = [Page(options[x][0],self.ui,[Title(self.ui,options[x][0]),*self.persisent_widgets]) for x in range(len(options))]
        self.first_page = Page("Menu",self.ui,[Title(self.ui,self.title_text),Menu(self,self.ui,options,self.pages),*self.persisent_widgets])
        self.pages.append(self.first_page)
        self.load_page("Menu")
    
    def restart_program(self):
        self.clear_page()
        self.load_page("Menu")
        

    def load_page(self,page_id):
        print("Loading page")
        for page in self.pages:
            if page.id == page_id:
                page.show()
            else:
                page.hide()
    
    def clear_page(self):
        for page in self.pages:
            page.hide()

    def exit_program(self):
        self.ui.destroy()

    def start_program(self):
        self.ui.mainloop()


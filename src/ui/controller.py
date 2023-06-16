import tkinter as tk
from tkinter import ttk
class UIController:
    def __init__(self,ui):
        self.ui = ui
        self.pages = []
    
    def clear_screen(self):
        for widget in self.ui.winfo_children():
            widget.destroy()

    def change_top_bar(self,colour):
        pass

    def change_page(self,page):
        pass



    
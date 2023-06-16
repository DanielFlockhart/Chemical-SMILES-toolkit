
class Page:
    def __init__(self, id,ui):
        self.id = id
        self.ui = ui
        self.components = []

    def show(self):
        self.ui.pack(fill="both", expand=True)

    def hide(self):
        self.ui.pack_forget()
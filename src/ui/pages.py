
class Page:
    def __init__(self, id,ui,components):
        self.id = id
        self.ui = ui
        self.components = components

    def hide(self):
        for component in self.components:
            try:
                component.hide()
            except:
                pass # If the component has no hide function, ignore it (It may be a tkinter widget)

    def show(self):
        for component in self.components:
            try:
                component.build()
            except:
                pass # If the component has no build function, ignore it (It may be a tkinter widget)
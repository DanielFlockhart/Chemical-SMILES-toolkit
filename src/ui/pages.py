
class Page:
    def __init__(self, id,ui,components):
        self.id = id
        self.ui = ui
        self.components = components

    def hide(self):
        for component in self.components:
            component.hide()

    def show(self):
        for component in self.components:
            component.build()
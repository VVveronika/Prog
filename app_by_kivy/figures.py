from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)

class Ellipse(Widget):
    pass
class Circle(Widget):
    pass
class Rectangle(Widget):
    pass


class FiguresApp(App):
    def build(self):
        root = GridLayout(cols = 3, padding = 20, spacing = 20)
        root.add_widget(Ellipse())
        root.add_widget(Circle())
        root.add_widget(Rectangle())
        return root
    
FiguresApp().run()
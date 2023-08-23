from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

Window.clearcolor = (1, 1, 1, 1)

class Ans1(TextInput):
    pass
class Ans2(TextInput):
    pass
class Ans3(Label):
    pass

class MyBL(BoxLayout):
    def changeText(self):
        self.ids.label.text = str(Ans1.text + Ans2.text)
        return MyBL()

class FiguresApp(App):
    def build(self):
        root = GridLayout(cols = 3, padding = 20, spacing = 20)
        root.add_widget(Ans1())
        root.add_widget(Ans2())
        root.add_widget(Ans3())
        return root

    
FiguresApp().run()
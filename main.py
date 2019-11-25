import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import json


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2


        self.add_widget(Label(text="wysokosc"))
        self.wys = TextInput(text=" ",multiline=False)
        self.wys.text = tak(1)
        self.add_widget(self.wys)

        self.add_widget(Label(text="pozycja"))
        self.poz = TextInput(text=" ",multiline=False)
        self.poz.text = tak(2)
        self.add_widget(self.poz)

        self.add_widget(Label(text="cisnienie"))
        self.cis = TextInput(text= " ",multiline=False)
        self.cis.text = tak(3)
        self.add_widget(self.cis)

        self.add_widget(Label(text="kierunek wiatru"))
        self.wia = TextInput(text= " ",multiline=False)
        self.wia.text = tak(4)
        self.add_widget(self.wia)

        self.add_widget(Label(text="predkosc"))
        self.vel = TextInput(text= ' ', multiline=False)
        self.vel.text = tak(5)
        self.add_widget(self.vel)

def tak(liczb):
    with open('przyklady.json') as f:
        data = json.load(f)
    for i in data['dane1']:
        new_string = i

    new_string1 = json.dumps(new_string)
    if liczb == 0:
        return (new_string['parameter'])
    if liczb == 1:
        return (new_string['height'])
    if liczb == 2:
        return (new_string['position'])
    if liczb == 3:
        return (new_string['Atmo_pressure'])
    if liczb == 4:
        return (new_string['Wind'])
    if liczb == 5:
        return (new_string['Velocity'])
    else:
        return None



class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()

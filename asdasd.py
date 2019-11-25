from kivy.garden.mapview import MapView, MapMarker
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.uix.button import Button
import random
from kivy.uix.gridlayout import GridLayout
import json

marker_source = './bajer2.png'


class Plane(Widget):
    def __init__(self, mapview):
        self.mapview = mapview
        self.m2 = 0

    def update(self, dt):
        m1 = MapMarker(lat=dane(2), lon=dane(3))
        # m1.source = marker_source
        self.mapview.add_marker(m1)
        if (self.m2):
            self.mapview.remove_marker(self.m2)
        self.m2 = m1
def dane(liczb):
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
        return (new_string['lat'])
    if liczb == 3:
        return (new_string['lon'])
    if liczb == 4:
        return (new_string['Wind'])
    if liczb == 5:
        return (new_string['Velocity'])
    else:
        return None

class MapViewApp(App):
    def build(self):
        self.root = GridLayout(
            rows=2)
        self.b1 = Button()
        # self.root.add_widget(self.b1)
        self.mapview = MapView(zoom=10, lat=51.144894309328016, lon=17.017822265625004)
        self.root.add_widget(self.mapview)
        self.plane = Plane(self.mapview)
        self.plane.update(1)
        #Clock.schedule_interval(self.plane.update, 1.0 / 1.0)
        return self.root


MapViewApp().run()

#  self.Europa = MapMarker(
#         lat=44.705362, lon=16.974940, source=marker_source)
#     self.mapview.add_marker(self.Europa)

#     self.mapview.remove_marker(self.Europa)
#     self.AmNorth = MapMarker(
#         lat=35.714325, lon=-107.40868, source=marker_source)
#     self.mapview.add_marker(self.AmNorth)

#     self.AmSouth = MapMarker(
#         lat=-25.787351, lon=-54.048190, source=marker_source)
#     self.mapview.add_marker(self.AmSouth)

#     self.Austria = MapMarker(
#         lat=-45.103914, lon=141.684269, source=marker_source)
#     self.mapview.add_marker(self.Austria)

#     self.Austria1 = MapMarker(
#         lat=-6.092218, lon=16.224152, source=marker_source)
#     self.mapview.add_marker(self.Austria1)
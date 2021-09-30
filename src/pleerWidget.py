import json

from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config

class PleerWidget(Widget):
    def __init__(self):
        with open('configs/settings.json') as json_file:
            self.__settings = json.load(json_file)

        #with open('configs/themes.json') as json_file:
        #    self.__theme = json.load(json_file)
        #    theme = str(self.__settings["theme"])
        #    self.__theme = self.__theme[theme]
        self.__theme = self.__settings["theme"]
        self.__settings = self.__settings["widgets"]["pleer"]

    def build(self):
        widgetLayout = StackLayout(spacing=10, padding=[10, 10, 10, 10])

        carousel = Carousel(direction='right', size_hint=(1.0, 0.9))

        for i in range(3):
            src = "http://placehold.it/480x270.png&text=slide-%d&.png" % i
            image = AsyncImage(source=src, allow_stretch=True)
            carousel.add_widget(image)
        
        widgetLayout.add_widget(carousel)

        buttonsLayout = BoxLayout(size_hint=(0.7, 0.1), pos_hint={"center_x":0.0})

        for i in ["pause", "volume_up", "volume_down", "mute", "next", "previous"]:
            buttonsLayout.add_widget(Button(text=i))

        widgetLayout.add_widget(buttonsLayout)
        
        return widgetLayout

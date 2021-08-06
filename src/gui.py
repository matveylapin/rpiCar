from config import *

from kivy.app import App
from kivy.uix.button import Button

from kivy.config import Config
Config.set('graphics', 'width', SCREEN_WIDTH)
Config.set('graphics', 'height', SCREEN_HEIGHT)
Config.write()

class MainApp(App):
    def build(self):
        return Button()
 
if __name__ == '__main__':
    MainApp().run()
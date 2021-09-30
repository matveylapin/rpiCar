from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config
Config.set('graphics', 'width', 1024)
Config.set('graphics', 'height', 768)
Config.write()

from pleerWidget import PleerWidget

class MainApp(App):
    def build(self):
        pageLayout = BoxLayout(orientation='vertical')
        pageLayout.add_widget(PleerWidget().build())
        pageLayout.add_widget(Button(size_hint=(1.0, 0.5)))
        return pageLayout
 
if __name__ == '__main__':
    MainApp().run()
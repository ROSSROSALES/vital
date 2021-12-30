from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import NumericProperty
import time


class MainWindow(Screen):
    def __init__(self):
        self.clock=Clock()


class Clock1(Label):
    def update(self, *args):
        self.text = time.asctime()

class ExtraWindow(Screen):
    pass

class Time(Label):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

class MyApp(App):
    def build(self):
        return kv

if __name__=="__main__":
    MyApp().run()



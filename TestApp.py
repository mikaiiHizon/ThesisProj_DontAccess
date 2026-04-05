import kivy
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.lang import Builder

class TestApp(MDApp):
    def build (self):
        return Label(text='Test Code')
    
if __name__ == '__main__':
    TestApp().run()
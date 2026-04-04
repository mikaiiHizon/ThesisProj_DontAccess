import kivy
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.lang import Builder

class TestApp(MDApp):
    def build (self):
        return Builder.load_string("""
MDBoxLayout:
    orientation: 'vertical'
    md_bg_color: 0.95, 0.95, 0.95, 1
    Label:
        text: "Test code"
""")
if __name__ == '__main__':
    TestApp().run()
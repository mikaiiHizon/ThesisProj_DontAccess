from kivy.lang import Builder
from kivymd.app import MDApp

# Use Builder to load a string or .kv file
KV = '''
MDScreen:
    MDLabel:
        text: "Hello, KivyMD!"
        halign: "center"
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()
from kivy.lang import Builder
from kivymd.app import MDApp

# Use Builder to load a string or .kv file
KV = '''
MDScreen:
    MDLabel:
        text: "Hello, KivyMD!"
        halign: "center"
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()

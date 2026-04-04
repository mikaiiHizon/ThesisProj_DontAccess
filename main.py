import kivy
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.pickers import MDDatePicker
from weather_manager import get_weather_data

Window.size = (350, 600)

class MainApp(MDApp):            
    def build (self):
        return Builder.load_file("main.kv")
    def update_weather(self):
        data = get_weather_data()
        self.root.ids.weather_info.text = f"Temp: {data['temp']}°C | Hum: {data['humidity']}% | {data['status']}"
        
        def run_prediction(self):
            self.root.ids.result_label.text = "Result: Ready to Predict"
        
if __name__ == '__main__':
    MainApp().run()
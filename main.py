import kivy
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import DictProperty
from kivymd.uix.pickers import MDDatePicker
from weather_manager import get_forecast_data

Window.size = (350, 600)

class MainApp(MDApp):            
    weather_data = DictProperty({})

    def get_weather_icon(self, cond):
        icons = {
            'Clear': 'weather-sunny',
            'Clouds': 'weather-cloudy',
            'Rain': 'weather-rainy',
            'Drizzle': 'weather-partly-rainy',
            'Thunderstorm': 'weather-lightning',
            'Snow': 'weather-snowy',
            'Mist': 'weather-fog'
        }
        return icons.get(cond, 'weather-cloudy')


    def build(self):
        return Builder.load_file("main.kv")
    
    def update_weather(self):
        data = get_forecast_data()
        self.weather_data = data
        self.root.ids.current_weather.text = f"Current: {data['current']['temp']}°C | {data['current']['humidity']}% | {data['current']['status']}"

    def run_prediction(self):
        self.root.ids.result_label.text = "Result: Ready to Predict"

        
if __name__ == '__main__':
    MainApp().run()


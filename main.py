from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from weather_manager import get_weather_data

Window.size = (350, 600)


class HomeScreen(Screen):
    def update_weather(self):
        data = get_weather_data()

        temp = data["temp"]
        humidity = data["humidity"]

        # Weather classification (AI-ready logic)
        if humidity > 80:
            condition = "Umuulan 🌧️"
            icon = "weather-rainy"
        elif temp > 30:
            condition = "Maaraw ☀️"
            icon = "weather-sunny"
        else:
            condition = "Maulap ☁️"
            icon = "weather-cloudy"

        self.ids.weather_icon.icon = icon
        self.ids.weather_info.text = f"{temp}°C | Humidity {humidity}%\n{condition}"


class ChatScreen(Screen):
    def send_message(self):
        msg = self.ids.user_input.text.strip()
        if not msg:
            return

        self.add_message(msg, "user")

        # PLACEHOLDER FOR YOUR AI MODEL (train_model.py later)
        bot_reply = "AI: Salamat! (ready for model integration 🤖)"
        self.add_message(bot_reply, "bot")

        self.ids.user_input.text = ""
        self.ids.scroll_view.scroll_y = 0

    def add_message(self, text, sender):
        from kivymd.uix.label import MDLabel

        msg = MDLabel(
            text=text,
            size_hint_y=None,
            height=40,
            halign="right" if sender == "user" else "left",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1) if sender == "user" else (0, 0, 0, 1),
            md_bg_color=(0.1, 0.4, 0.1, 1) if sender == "user" else (0.9, 0.9, 0.9, 1),
            padding=(10, 10)
        )

        self.ids.chat_box.add_widget(msg)


class AddScreen(Screen):
    pass


class ListScreen(Screen):
    pass


class MainApp(MDApp):
    def build(self):
        return Builder.load_file("main.kv")

    def change_screen(self, screen):
        self.root.current = screen


if __name__ == "__main__":
    MainApp().run()
# Your app starts here. Press Run (F5) and it opens in the "Your app's window" tab.
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class Screen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=40, spacing=20, **kwargs)
        self.presses = 0
        self.label = Label(text="Press the button", font_size=32)
        button = Button(text="Press me", font_size=28, size_hint=(1, 0.4))
        button.bind(on_press=self.pressed)
        self.add_widget(self.label)
        self.add_widget(button)

    def pressed(self, button):
        self.presses += 1
        self.label.text = f"Pressed {self.presses} time{'s' if self.presses != 1 else ''}"


class MyApp(App):
    def build(self):
        self.title = "My app"
        return Screen()


if __name__ == "__main__":
    MyApp().run()

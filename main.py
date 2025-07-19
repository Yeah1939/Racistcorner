from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TestScreen1(name="test_screen_1"))
        sm.add_widget(TestScreen2(name="test_screen_2"))
        return sm
class TestScreen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        button1 = Button(text="kill nigger")
        button2 = Button(text="kill jew")
        button2.on_press = self.any_window
        self.count = 0
        button1.on_press = self.test
        self.label1 = Label(text= "Racist.exe")
        layout = BoxLayout(orientation= "vertical",padding = 10,spacing = 20)
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(self.label1)

        self.add_widget(layout)

    def test(self):
        self.count += 1
        self.label1.text = str(self.count)
    def any_window(self):
        self.manager.current = "test_screen_2"

class TestScreen2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        label = Label(text = "Nazi Corner")
        button = Button(text = "back")
        layout = BoxLayout()
        button.on_press = self.back
        layout.add_widget(label)
        layout.add_widget(button)

        self.add_widget(layout)
    def back(self):
        self.manager.current = "test_screen_1"
obj = MyApp()
obj.run()

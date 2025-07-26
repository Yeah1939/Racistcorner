# напиши тут свою програму
# напиши тут свою програму
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import instructions

class MainWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        text = Label(text= instructions.txt_instruction)

        name_label = Label(text = "Введіть імя")
        age_label = Label = Label(text = "Введіть вік")
        self.name_user = TextInput(multiline= False)
        self.age = TextInput(multiline= False)
        self.button = Button(text = "Продовжити")
        self.button.on_press = self.next

        layout_name = BoxLayout()
        layout_age = BoxLayout()
        layout_name.add_widget(name_label)
        layout_name.add_widget(self.name_user)
        layout_age.add_widget(age_label)
        layout_age.add_widget(self.age)

        main_layout = BoxLayout(orientation = "vertical")
        main_layout.add_widget(text)
        main_layout.add_widget(layout_name)
        main_layout.add_widget(layout_age)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)

    def next(self):
        self.manager.current = "first_pulse"

class InputPulseFirst(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        text = Label(text= instructions.txt_test1)

        result_label = Label(text="Введіть результат")
        self.first_result = TextInput(multiline= False)
        self.button = Button(text = "Продовжити")
        self.button.on_press = self.next

        layout_result = BoxLayout()
        layout_result.add_widget(result_label)
        layout_result.add_widget(self.first_result)

        main_layout = BoxLayout(orientation = "vertical")
        main_layout.add_widget(text)
        main_layout.add_widget(layout_result)
        main_layout.add_widget(self.button)

    def next(self):
        global first_result
        first_result = self.first_result.text
        self.manager.current = "sits"

class SitsWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        text = Label(text= instructions.txt_sits)
        self.button = Button(text = "Продовжити")
        self.button.on_press = self.next

        main_layout = BoxLayout(orientation = "vertical")
        main_layout.add_widget(text)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)
    
    def next(self):
        self.manager.current = "second_pulse"

class InputPulseSecond(Screen):
    def __init__(self, **kwargs):
        super().init(**kwargs)

        text = Label(text= instructions.txt_test3)

        second_result_label = Label(text = "результат")
        third_result_label = Label(text = "Рез після відпочинку")
        self.second_result = TextInput(multiline= False)
        self.third_result = TextInput(multiline= False)
        self.button = Button(text= "Продовжити")
        self.button.on_press = self.next

        layout_first_result = BoxLayout()
        layout_second_result = BoxLayout()
        layout_first_result.add_widget(second_result_label)
        layout_first_result.add_widget(self.second_result)
        layout_second_result.add_widget(third_result_label)
        layout_second_result.add_widget(self.third_result)

        main_layout = BoxLayout(orintation="vertical")
        main_layout.add_widget(text)
        main_layout.add_widget(layout_first_result)
        main_layout.add_widget(layout_second_result)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)


    def next(self):
        global second_result,third_result
        second_result = self.second_result.text
        third_result = self.third_result.text
        self.manager.current = "result"

class Result(Screen):
    def init(self, **kwargs):
        super().__init__(**kwargs)

        self.result = Label()
        self.on_enter = self.before
        self.add_widget(self.result)

    def before(self):
        self.result.text = f"{first_result} {second_result} {third_result}"

class Ruffier(App):
    def build(self):
        sm = ScreenManager
        sm.add_widget(MainWindow(name="main"))
        sm.add_widget(InputPulseFirst(name="first_pulse"))
        sm.add_widget(SitsWindow(name="sits"))
        sm.add_widget(InputPulseSecond(name="second_pulse"))
        sm.add_widget(Result(name="result"))

        return sm
    
ruffier = Ruffier()
ruffier.run()

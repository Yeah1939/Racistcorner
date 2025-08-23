# напиши тут свою програму
# напиши тут свою програму
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import instructions
from seconds import Seconds
from sits import Sits
from runner import Runner
from ruffier import *

Window.clearcolor = (0.67,0.3,0.2,1)
WIDTH,HEIGHT = 1939 //3 , 1945 // 3

def check_int(value):
    try:
        return int(value)
    except:
        return False

class MainWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        text = Label(text= instructions.txt_instruction,text_size =(WIDTH,200))

        name_label = Label(text = "Введіть імя")
        age_label = Label(text = "Введіть вік")
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

        self.next_screen = False




        self.timer = Seconds(3)
        self.timer.bind()
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
        main_layout.add_widget(self.timer)
        main_layout.add_widget(layout_result)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)

    def sec_finish(self,*arg):
        self.next_screen = True
        self.button.set_disabled(False)
        self.first_result.set_disabled(False)
        self.button.text = "Продовжити"

    def next(self):
        if self.next_screen == False:
            self.timer.start()
            self.button.set_disabled(True)
        else:
            global first_result
            first_result = check_int(self.first_result.text)
            if first_result == False or first_result < 0:
                self.first_result.text = "0"
            else:
                self.manager.current = "sits"

class SitsWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False

        text = Label(text= instructions.txt_sits)
        self.runner = Runner(5)
        self.runner.bind(finished = self.run_finished)
        self.sits = Sits(5)



        self.button = Button(text = "Продовжити")
        self.button.on_press = self.next

        f_v_layout = BoxLayout(orientation= "vertical")
        f_v_layout.add_widget(text)

        h_layout = BoxLayout()
        h_layout.add_widget(f_v_layout)
        h_layout.add_widget(self.runner)

        main_layout = BoxLayout(orientation = "vertical")
        main_layout.add_widget(h_layout)
        main_layout.add_widget(self.sits)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)
    def run_finished(self,*args):
        self.button.set_disabled(False)
    
    def next(self):
        if self.next_screen == False:
            self.button.set_disabled(True)
            self.runner.start()
            self.runner.bind(value= self.sits.next)
        else:
            self.manager.current = "second_pulse"

class InputPulseSecond(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        self.check_timer = 0

        text = Label(text= instructions.txt_test3)
        self.timer = Seconds(3)
        self.timer.bind(done= self.sec_finish)
        self.instruction = Label(text="")



        second_result_label = Label(text = "результат")
        third_result_label = Label(text = "Рез після відпочинку")
        self.second_result = TextInput(multiline= False)
        self.second_result.set_disabled(True)
        self.third_result = TextInput(multiline= False)
        self.third_result.set_disabled(True)
        self.button = Button(text= "Почати")
        self.button.on_press = self.next

        layout_first_result = BoxLayout()
        layout_second_result = BoxLayout()
        layout_first_result.add_widget(second_result_label)
        layout_first_result.add_widget(self.second_result)
        layout_second_result.add_widget(third_result_label)
        layout_second_result.add_widget(self.third_result)

        main_layout = BoxLayout(orientation="vertical")
        main_layout.add_widget(text)
        main_layout.add_widget(timer)
        main_layout.add_widget(layout_first_result)
        main_layout.add_widget(layout_second_result)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)

    def sec_finish(self,*args):
        if self.timer.done == True:
            if self.check_timer == 0:
                self.second_result.set_disabled(False)
                self.check_timer = 1
                self.instruction.text = "Відпочивайте"
                self.timer.restart(5)
            elif self.check_timer == 1:
                self.check_timer = 2
                self.instruction.text = "Міряйте пульс"
                self.timer.restart(3)
            elif self.check_timer == 2:
                self.third_result.set_disabled(False)
                self.button.set_disabled(False)
                self.instruction.text = "Впишіть результати пульсу"
                self.button.text = "Закінчити"
                self.next_screen = True


    def next(self):
        if self.next_screen == False:
            self.timer.start()
            self.instruction.text = "Міряйте пульс"
            self.button.set_disabled(False)
        else:
            global second_result,third_result
            second_result = check_int(self.second_result.text)
            third_result = check_int(self.third_result.text)
            if second_result == False or second_result <0:
                self.second_result.text = "0"
            elif third_result == False or third_result <0:
                self.third_result.text = "0"
            else:
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
        Window.size = WIDTH,HEIGHT
        sm = ScreenManager()
        sm.add_widget(MainWindow(name="main"))
        sm.add_widget(InputPulseFirst(name="first_pulse"))
        sm.add_widget(SitsWindow(name="sits"))
        sm.add_widget(InputPulseSecond(name="second_pulse"))
        sm.add_widget(Result(name="result"))

        return sm
    
ruffier = Ruffier()
ruffier.run()

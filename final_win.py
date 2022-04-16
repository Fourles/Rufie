# напиши здесь код третьего экрана приложения
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
global p1,p2,p3,age
        
p1 = 0
p2 = 0
p3 = 0
age = 7
def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False

def test(p1, p2, p3):
    index = (4*(p1+p2+p3) -200)/10
    return index

def result_index(index, age):
    s = 'Неизвестный результат'
    i = 0
    if age <= 8:
        i = 0
    elif age <=10:
        i = 1
    elif age <= 12:
        i = 2
    elif age <=14:
        i = 3
    else:
        i = 4
    index += 1.5*i
    if index < 6:
        s = "Отличный результат! Ваше сердце работает как часы!"
    elif index < 12:
        s = "Хороший результат! Сердце работает хорошо, но не стоит злоупотреблять."
    elif index < 17:
        s = "Результат удовлетворительный. Но следует тщательнее следить за здоровьем"
    elif index < 21:
        s = "Результат слабый. Рекомендовано обращение к доктору."
    else:
        s = 'Результат ужасный. Обследуйтесь у врача как можно скорее!!!'
    
    return s



class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__( **kwargs)
        mainLab = Label(text = "Тут будет Название приложения")
        btnTest = Button(text = "Пройти Тест")
        btnTest.on_press = self.nextTest
        btnInst = Button(text = "Инструкция")
        btnInst.on_press = self.nextInst
        btnExit = Button(text = "Выход")
        btnExit.on_press = self.exit_app
        h1 = BoxLayout(orientation = "horizontal", padding = 20, spacing = 10)
        h2 = BoxLayout(orientation = "vertical", padding = 20, spacing = 10)

        v1 = BoxLayout(orientation = "vertical", padding = 20, spacing = 10)
        h1.add_widget(mainLab)
        h2.add_widget(btnTest)
        h2.add_widget(btnInst)
        h2.add_widget(btnExit)

        v1.add_widget(h1)
        v1.add_widget(h2)
        self.add_widget(v1)
    def nextInst(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'instructions'
    def nextTest(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'test'
    def exit_app(self):
        app.stop()
class InstructionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        head = Label(text = "Инструкция" , halign='center')
        hline1 = BoxLayout()
        body = Label(text = 'Измерять надо так-то так-то', halign='center')
        hline = BoxLayout()
        btnBack = Button(text = "На главный экран")
        btnBack.on_press = self.backMain
        vmain = BoxLayout(orientation = 'vertical', padding = 20, spacing = 10)
        vmain.add_widget(head)
        vmain.add_widget(hline)
        vmain.add_widget(body)
        vmain.add_widget(hline1)
        vmain.add_widget(btnBack)
        self.add_widget(vmain)
    def backMain(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main'

class TestScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ageLab = Label(text = "Возраст:", halign='center')
        self.ageInput = TextInput(text = "0", multiline=False)
        firstLab = Label(text = "Первое измерение: \nСостояние покоя",halign='center')
        self.firstInput = TextInput(text = "0", multiline=False)
        secondLab = Label(text = "Второе измерение: \nСостояние активности",halign='center')
        self.secondInput = TextInput(text = "0", multiline=False)
        thirdLab = Label(text = "Третье измерение: \nСостояние восстановления",halign='center')
        self.thirdInput = TextInput(text = "0", multiline=False)
        btnNext = Button(text = "Рассчитать результаты:")
        btnNext.on_press = self.nextRes

        
        vmain = BoxLayout(orientation = 'vertical', padding = 20, spacing = 10)
        v1 = BoxLayout(orientation = 'vertical', padding = 20, spacing = 10)
        v2 = BoxLayout(orientation = 'vertical', padding = 20, spacing = 10)
        v3 = BoxLayout(orientation = 'vertical', padding = 20, spacing = 10)
        v4 = BoxLayout(orientation = 'vertical', padding = 20, spacing = 10)
        v1.add_widget(ageLab)
        v1.add_widget(self.ageInput)
        v2.add_widget(firstLab)
        v2.add_widget(self.firstInput)
        v3.add_widget(secondLab)
        v3.add_widget(self.secondInput)
        v4.add_widget(thirdLab)
        v4.add_widget(self.thirdInput)

        vmain.add_widget(v1)
        vmain.add_widget(v2)
        vmain.add_widget(v3)
        vmain.add_widget(v4)
        vmain.add_widget(btnNext)
        self.add_widget(vmain)
    def nextRes(self):
        global p1,p2,p3,age
        
        age = check_int(self.ageInput.text)
        p1 = check_int(self.firstInput.text)
        p2 = check_int(self.secondInput.text)
        p3 = check_int(self.thirdInput.text)
        
        normaldata = (age != False and age > 0) and (p1 != False and p1 > 0) and (p2 != False and p2 > 0) and (p3 != False and p3 > 0)
        if normaldata:
            self.manager.transition.direction = 'left'            
            self.manager.current = 'result'
            
class ResultScreen(Screen):
    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)
        
        global p1,p2,p3,age
        
        index = test(p1,p2,p3)
        advice = result_index(age, index)
        self.indexLab = Label(text = "Ваш индекс Руфье:")
        self.levelLab = Label(text = str(index))
        self.adviceLab = Label(text = advice)
        btnBack = Button(text = "На главный экран")
        btnBack.on_press = self.backMain
        vmain = BoxLayout(orientation = 'vertical', padding = 20, spacing = 10)
        vmain.add_widget(self.indexLab)
        vmain.add_widget(self.levelLab)
        vmain.add_widget(self.adviceLab)
        vmain.add_widget(btnBack)
        self.add_widget(vmain)
        self.on_enter = self.res
    def backMain(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main'
        global p1,p2,p3,age
        age = 0
        p1 = 0
        p2 = 0
        p3 = 0
    def res(self):
        global p1,p2,p3,age
        index = test(p1,p2,p3)
        self.levelLab.text = str(index)
      
        self.adviceLab.text = result_index(index,age)

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        main = MainScreen(name = 'main')
        test = TestScreen(name = 'test')
        result = ResultScreen(name = 'result')              
        instructions = InstructionScreen(name = 'instructions')
        sm.add_widget(main)
        sm.add_widget(test)
        sm.add_widget(result) 
        sm.add_widget(instructions)
        return sm

app = MyApp()
app.run()

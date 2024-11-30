import json
import gspread
import os
import sys
from kivy.uix.accordion import FloatLayout
from kivy.uix.accordion import ObjectProperty
from kivy.uix.effectwidget import Rectangle
from kivy.uix.stacklayout import StackLayout
from kivy.uix.progressbar import ProgressBar
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import NoTransition
from kivy.properties import ObjectProperty
from datetime import datetime
from kivy.core.window import Window
    
    
#Для зміни тем
#with open('tests.json','r') as file:  
#    current_theme = json.load(file)






class MainMenu(ScreenManager):
    lesson_text=StringProperty('')
    #Функція для отримання часу та тексту головного екрану
    def get_time():
        global current_lesson
        #Час кінця та початку всіх 8 уроків в форматі "хвилини від 00:00"
        lessons_time =[
                    (510, 555), 
                    (565, 610), 
                    (630, 675), 
                    (685, 730), 
                    (740, 785), 
                    (805, 850), 
                    (870, 915), 
                    (920, 965)
                    ]
        #Поточний час в форматі "хвилини від 00:00"
        current_time = datetime.now().hour*60 + datetime.now().minute
        current_lesson = 'Nothing'
        end_time = (0,0)
        next_lesson_time = (8,30)
        #Основне розгалуження, визначення чи є поточний час до 1/після останнього уроку
        if current_time>=965 or current_time<=510:
            current_lesson='No'
            next_lesson_time=(8,30)
        else:
            #Вхід в for цикл для визначення який конкретно йде урок, і чи йде він взагалі
            for i in range(len(lessons_time)):
                #Визначення який зараз урок
                if current_time<=lessons_time[i][0] or current_time>=lessons_time[i][1]:
                    #Зараз перерва
                    current_lesson = 'No'
                elif current_time<=lessons_time[i][1]:
                    #Зараз є урок
                    if i<7:
                        current_lesson = i+1
                        end_time = (lessons_time[i][1]//60, lessons_time[i][1]%60)
                        next_lesson_time = (lessons_time[i+1][0]//60, lessons_time[i+1][0]%60)
                        break
                    else:
                        current_lesson = i+1
                        end_time = (lessons_time[i][1]//60, lessons_time[i][1]%60)
                        next_lesson_time=(8,30)
                        break
                    
        #Перевірка для уникнення помилки типу "16:0"
        end_time= (end_time[0],'00' if end_time[1]==0 else '0'+str(end_time[1]) if end_time[1]<10 else end_time[1])
        next_lesson_time= (next_lesson_time[0],'00' if next_lesson_time[1] == 0 else next_lesson_time[1])
        
        #Розгалуження для випису даних, отриманих в циклі на головний екран
        if current_lesson == 'No':
            #Якщо уроку немає
            lessons_text=f'''     Зараз немає уроку
  Наступний урок о {next_lesson_time[0]}:{next_lesson_time[1]}'''
            
        else:
            #Якщо урок є
            lessons_text=f'''    Урок закінчується о {end_time[0]}:{end_time[1]}
                      ({current_lesson} урок)
       Наступний урок о {next_lesson_time[0]}:{next_lesson_time[1]}'''
       #Повернення тексту
        return(lessons_text)
    #Встановлення цього тексту в змінну ScreenManager`a
    lesson_text=get_time()

print(current_lesson)
#Запуск програми
class KRLApp(App):
    def reload(self):
        self.stop()
        if __name__ == '__main__':
            KRLApp().run()
    #Зміна тем:
    
    global current_theme
    with open('tests.json','r') as file:
        current_theme = json.load(file)
    
    if current_theme == 'black':
        theme = {
            'background_color':(0,0,0,1)
        }
    else:
        theme = {
            'background_color':(1,1,1,1)
        }
    def change_theme(self):
        global current_theme
        global theme
        if current_theme =='black':
            with open('tests.json','w') as file:
                json.dump('white',file)
            with open('tests.json','r') as file:
                current_theme = json.load(file)
            theme = {
                'background_color':(0,0,0,1)
            }
            print(current_theme)
        else:
            with open('tests.json','w') as file:
                json.dump('black',file)
            with open('tests.json','r') as file:
                current_theme = json.load(file)
            theme = {
                'background_color':(1,1,1,1)
            }
            print(current_theme)
        print(theme)
        
    #Функція для встановлення розміру та назви
    def build(self):
        
        self.title='KRL App'
        Window.size = (330,650)
        Window.stretch = False
        return(MainMenu())

    

class ActionBarWHB(BoxLayout):
    pass
    
    
if __name__ == '__main__':
    KRLApp().run()
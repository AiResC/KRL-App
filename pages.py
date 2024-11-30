from kivy.uix.filechooser import ScreenManager
from kivy.uix.actionbar import BoxLayout
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty
from webbrowser import open
from webbrowser import open_new_tab
from kivy.uix.screenmanager import Screen

Builder.load_file('pages.kv')

class Cons(ScreenManager):
    pass

class Library(ScreenManager):
    pass

class Bells(BoxLayout):
    pass

class List(ScreenManager):
    pass

class Setting(BoxLayout):
    pass

class Social(BoxLayout):
    def open_facebook(self):
        open('https://www.facebook.com/volsikiev/?locale=ru_RU')
    def open_telegram(self):
        open('https://t.me/KRLyceum')
    def open_tiktok(self):
        open('https://www.tiktok.com/@krlyceum')
    def open_instagram(self):
        open('')

class LessonForBells(BoxLayout):
    lesson_number = StringProperty('')
    lesson_time = StringProperty('')

class BreakForBells(BoxLayout):
    time = StringProperty('')

class EatForBells(BoxLayout):
    kind = StringProperty('')
    time = StringProperty('')

class TwoClasses(BoxLayout):
    class1 = StringProperty('')
    class2 = StringProperty('')
    
class OneClass(BoxLayout):
    class1 = StringProperty('')
    
class TwoClassesLibrary(BoxLayout):
    class1 = StringProperty('')
    class2 = StringProperty('')
    class11 = StringProperty('')
    class22 = StringProperty('')
    
class OneClassLibrary(BoxLayout):
    class1 = StringProperty('')
    class11 = StringProperty('')
    
class BookButton(BoxLayout):
    book = StringProperty('')
    link = StringProperty('')
    def open_link(self,link):
        open_new_tab(str(link))
        
class Day(BoxLayout):
    day = StringProperty('')

    
    
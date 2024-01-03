from kivy.app import App
from kivy.uix.label import Label
class MyApp(App):
    def build(self):
        #return Label(text="hello world")
        return Label(text="hello world", font_size='50',color="pink")
if __name__ == '__main__':
    MyApp().run()






    





from kivy.app import App
from kivy.uix.label import Label
#from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
 
class MyApp(App):
    def build(self):
        #layout = BoxLayout(orientation="vertical")
        #label1 = Label(text="hello world",font_size = '100')
        #label2 = Label(text="My Guys!!!!", font_size='50')
        #button = Button(text="PRESS")
        #layout.add_widget(label1)
        #layout.add_widget(label2)
        #layout.add_widget(button)


        layout = FloatLayout()
        label1 = Label(text='Hello', size_hint = (0.3 ,0.2),pos_hint=('center_x':0.2,'center_y':0.5))
        label2 = Label(text = 'Happy New Year',size_hint = (0.5,0.7), pos_hint = ('center_x':0.5,'center_y':0.1))
        layout.add_widget(label1)
        layout.add_widget(label2)



        return layout
    

if __name__ == '__main__':
    MyApp().run()






    





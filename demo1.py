import numpy as np

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.uix.button import Button


from kivy.clock import Clock


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.orientation='vertical'
        
        self.title = MyLabel(text=
                            'Welcome to NumScriber', 
                            #size_hint=(1, .1), 
                            font_size= '20sp', 
                            color=[0.85,0.85,0.85,1],
                            valign='middle',
                            halign='center'
                            )
        self.title.col = (0.3, 0.5, .7, 1)
        self.title_boxlayout = BoxLayout(orientation='vertical',
                             size_hint=(1, .1)
                             )
        self.title_boxlayout.add_widget(self.title)
        self.add_widget(self.title_boxlayout)
        
        self.subtitle = MyLabel(text=
                            'Please press the button!', 
                            size_hint=(1, 0.2),
                            font_size= '{}sp'.format(24), 
                            color=[0.95,0.95,0.95,1],
                            valign='middle',
                            halign='center',
                            )
        self.subtitle.col = (0.3, 0.7, 1, .8)
        self.sub_lyot =                                                                     BoxLayout(orientation='vertical',
                                       size_hint=(1, 0.8))
        self.sub_lyot.add_widget(self.subtitle)
        self.add_widget(self.sub_lyot)
        
        self.d=NewWidget()
        
        self.d.bind(numx=self.update_label)
        
        self.num_bar = MyLabel(
                                    text=str(self.d.numx),
                                    size_hint= (1, .8),
                                    font_size= '{}sp'.format(80),
                                    color=[1,1,.85,1],
                                    valign='middle',
                                    halign='center'
                                    )
        self.num_bar.col = (0.6, 0.55, .55, 1)
        
        self.sub_lyot.add_widget(self.num_bar)
        
        
        
        self.b1 = Button(text ="Push Me !",
                   font_size ="20sp",
                   background_color =(1, 1, 1, 1),
                   color =(1, 1, 1, 1),
                   size =(32, 32),
                   size_hint =(1, .2),
                   #pos =(300, 2))
                   )
        self.add_widget(self.b1)
        self.b1.bind(on_release=self.d.stopwatch)
        
        self.b2 = Button(text ="YAB !",
                   font_size ="20sp",
                   background_color =(1, 1, 1, 1),
                   color =(1, 1, 1, 1),
                   size =(32, 32),
                   size_hint =(1, .2),
                   #pos =(300, 2))
                   )
        self.add_widget(self.b2)
        self.b2.bind(on_release=self.update_subtitle)
        
        
    
    def update_label(self, instance, value):
        self.num_bar.text = (f'{value//100} : {value%100}')
    
    def update_subtitle(self, instance):
        self.subtitle.text = str(self.d.numx)


class NewWidget(Widget):
    numx = NumericProperty(0)
    
    
    def __init__(self, **kwargs):
        super(NewWidget, self).__init__(**kwargs)
        #self.gen_num()
        self.on=False
        
    def gen_num(self,*args):
        #self.numx= np.random.randint(0,10)
        self.numx +=1
        print(f'num ={self.numx}')
        
    def stopwatch(self, *args):
        if not self.on:
            self.xx = Clock.schedule_interval(self.gen_num, .001)
            self.on =True
        else:
            self.xx.cancel()
            self.on = False


class MyLabel(Label):
    col=(0.5,0.5,0.5,1)
    def on_size(self, *args):
        #self.text_size = self.size
        a,b,c,d = self.col
        #self.canvas.before.clear()
        with self.canvas.before:
            Color(a,b,c,d)
            Rectangle(pos=self.pos, size=self.size)




class Demo1App(App):
    def build(self):
        return MainLayout()
        	    
        
if __name__ in ('__main__'):
    Demo1App().run()
    
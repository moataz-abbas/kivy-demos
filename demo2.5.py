# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 11:47:01 2021

@author: mizo_
"""

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
        self.sub_lyot = BoxLayout(orientation='vertical',
                                       size_hint=(1, 0.8))
        self.sub_lyot.add_widget(self.subtitle)
        self.add_widget(self.sub_lyot)
        
        self.d=NewWidget()
        
        self.d.bind(numx=self.update_label)
        
        self.num_bar = MyLabel(text=str(self.d.numx),
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
        
        self.b3 = Button(text ="Reset",
                   font_size ="20sp",
                   background_color =(1, 1, 1, 1),
                   color =(1, 1, 1, 1),
                   size =(32, 32),
                   size_hint =(1, .2),
                   #pos =(300, 2))
                   )
        self.add_widget(self.b3)
        self.b3.bind(on_release=self.reset)
        
        
    
    def update_label(self, *args):
        #self.ds= value%100
        
        
        self.st = f'{np.char.zfill(str(self.d.s), 2)}'
        self.mt = f'{np.char.zfill(str(self.d.m), 2)}'
        self.t = (self.mt + ' : ' + self.st)
        self.num_bar.text = self.t

    
#def step_up(self):
        
        
    
    def update_subtitle(self, *args):
        self.subtitle.text = str(self.t)
        
    def reset(self, *args):
        self.d.s = 0
        self.d.m = 0
        self.update_label()

class NewWidget(Widget):
    numx = NumericProperty(0)
    
    
    def __init__(self, **kwargs):
        super(NewWidget, self).__init__(**kwargs)
        self.on=False
        self.s = 0
        self.m = 0
        self.h = 0
        
    def stepper(self,*args):
        self.numx +=1
        if self.numx == 60:
            self.m += 1
            self.s = 0
            self.numx = 0
        else:
            self.s = self.numx
        
        print(f'num = {self.numx}')
        
    def stopwatch(self, *args):
        if not self.on:
            self.xx = Clock.schedule_interval(self.stepper, 1)
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
    
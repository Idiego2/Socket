# qpy:kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.slider import Slider
import conex


class myApp(App):
    conn = conex.Conexao("localhost", 5000)

    def acender(self, value):
        self.conn.enviar('acender')

    def enviaSlide(self, arg, value):
        self.conn.enviar('s|'+str(value))

    def build(self):
        layout = BoxLayout(orientation='vertical', padding=0)
        titulo = BoxLayout(orientation='horizontal', padding=0)

        titulo.add_widget(Image(source="img/HomeAutomation.png", size_hint_x=None, width=200, padding=10))
        titulo.add_widget(Label(text="Automacao Residencial", font_size=('30sp'), halign='left'))

        lampada = BoxLayout(orientation='horizontal', padding=4)
        lampada.add_widget(Image(source="img/lightOff.png", size_hint_x=None, width=200, padding=10))
        lampada.add_widget(Label(text="Lampada", font_size=('20sp'), halign='left'))
        btnLigar = Button(text='Acender/Apagar')

        btnLigar.bind(on_press=self.acender)

        lampada.add_widget(btnLigar)

        servo = BoxLayout(orientation='horizontal', padding=4, backgroung='red')
        servo.add_widget(Image(source="img/carro.png", size_hint_x=None, width=200, padding=20))
        servo.add_widget(Label(text="Servo", font_size=('20sp'), halign='left'))
        slide = Slider(min=0, max=100, value=0, step=1)

        slide.bind(value=self.enviaSlide)
        servo.add_widget(slide)

        layout.add_widget(titulo)
        layout.add_widget(lampada)
        layout.add_widget(servo)

        return layout


myApp().run()
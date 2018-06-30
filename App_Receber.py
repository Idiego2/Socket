# qpy:kivy

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from conexao import Conexao


class myApp(App):
    cliente = Conexao("localhost", 5000)
    cliente.cliente()

    dadosTemperatura= Label(text="25 C", font_size=('40sp'))
    dadosNivel = Label(text="Nivel", font_size=('40sp'), halign='left')
    dadosPorta = Label(text="Porta", font_size=('40sp'), halign='left')
    dadosLuminosidade = Label(text="Luminosidade", font_size=('40sp'), halign='left')

    def atualizar(self, value):
        self.cliente.enviar('l')

        dados = self.cliente.receber()
        print dados
        dadosRecebidos = dados.split("|")

        self.dadosTemperatura.text=dadosRecebidos[0]
        self.dadosNivel.text=dadosRecebidos[1]
        self.dadosPorta.text=dadosRecebidos[2]
        self.dadosLuminosidade.text=dadosRecebidos[3]


    def build(self):
        layout = BoxLayout(orientation='vertical', padding=0)
        titulo = BoxLayout(orientation='horizontal', padding=0)

        titulo.add_widget(Image(source="img/HomeAutomation.png", size_hint_x=None, width=200, padding=10))
        titulo.add_widget(Label(text="Automacao Residencial", font_size=('30sp'), halign='left'))


        temperatura = BoxLayout(orientation='horizontal', padding=4, backgroung='red')
        temperatura.add_widget(Image(source="img/thermomete.png", size_hint_x=None, width=200, padding=20))
        temperatura.add_widget(Label(text="Temperatura", font_size=('30sp')))
        temperatura.add_widget(self.dadosTemperatura)

        nivel = BoxLayout(orientation='horizontal', padding=4, backgroung='red')
        nivel.add_widget(Image(source="img/level2.png", size_hint_x=None, width=200, padding=20))
        nivel.add_widget(Label(text="Nivel", font_size=('30sp'), halign='left'))
        nivel.add_widget(self.dadosNivel)

        porta = BoxLayout(orientation='horizontal', padding=4, backgroung='red')
        porta.add_widget(Image(source="img/porta.png", size_hint_x=None, width=200, padding=20))
        porta.add_widget(Label(text="Porta", font_size=('30sp')))
        porta.add_widget(self.dadosPorta)

        luminosidade = BoxLayout(orientation='horizontal', padding=4, backgroung='red')
        luminosidade.add_widget(Image(source="img/luminosidade.png", size_hint_x=None, width=200, padding=20))
        luminosidade.add_widget(Label(text="Luminosidade", font_size=('30sp')))
        luminosidade.add_widget(self.dadosLuminosidade)

        layout.add_widget(titulo)
        layout.add_widget(temperatura)
        layout.add_widget(nivel)
        layout.add_widget(porta)
        layout.add_widget(luminosidade)

        return layout

    def on_start(self):
        Clock.schedule_interval(self.atualizar,5)

myApp().run()
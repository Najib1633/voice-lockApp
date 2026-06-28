from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
import random

class VoiceLockScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(VoiceLockScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [30, 50, 30, 50]
        self.spacing = 20
        
        # Saita kalar bango ta amfani da lambobin RGBA
        Window.clearcolor = (0.95, 0.95, 0.98, 1)
        
        self.label_title = Label(
            text="Najif Voice Lock v1.0",
            font_size='24sp',
            color=(0.1, 0.1, 0.2, 1),
            bold=True,
            size_hint_y=None,
            height=50
        )
        self.add_widget(self.label_title)
        
        self.status = Label(
            text="A shirye don saita tsaro...",
            font_size='16sp',
            color=(0.4, 0.4, 0.5, 1),
            halign='center'
        )
        self.add_widget(self.status)
        
        self.btn_enroll = Button(
            text="1. Yi Rijistar Murya",
            font_size='18sp',
            background_normal='',
            background_color=(0.15, 0.65, 0.27, 1),
            size_hint_y=None,
            height=60
        )
        self.btn_enroll.bind(on_press=self.enroll_voice)
        self.add_widget(self.btn_enroll)
        
        self.btn_verify = Button(
            text="2. Gwada Bude Wayar",
            font_size='18sp',
            background_normal='',
            background_color=(0, 0.47, 1, 1),
            size_hint_y=None,
            height=60
        )
        self.btn_verify.bind(on_press=self.verify_voice)
        self.add_widget(self.btn_verify)
        
        self.registered_data = None

    def enroll_voice(self, instance):
        self.status.text = "Ina sauraro... Fadi kalmar sirrin!"
        self.registered_data = [random.random() for _ in range(5)]
        self.status.text = "Rijistar muryar Najif ta kammala! ✅"
        self.status.color = (0.1, 0.6, 0.2, 1)

    def verify_voice(self, instance):
        if not self.registered_data:
            self.status.text = "Haba! Yi rijista tukunna mana."
            self.status.color = (0.8, 0.1, 0.1, 1)
            return
            
        # Kwaikwayon tantance muryar
        if random.choice([True, False]):
            self.status.text = "ACCESS GRANTED! 🔓\nBarka da zuwa babban Injiniya!"
            self.status.color = (0.1, 0.6, 0.2, 1)
        else:
            self.status.text = "ACCESS DENIED! 🔒\nMuryar ba ta yi daidai ba."
            self.status.color = (0.8, 0.1, 0.1, 1)

class MainApp(App):
    def build(self):
        return VoiceLockScreen()

if __name__ == '__main__':
    MainApp().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.slider import Slider
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.config import Config
from kivy.utils import platform
from kivy.clock import Clock
import requests
import json
import os

# Window settings initialization
Window.softinput_mode = 'below_target'
Config.set('graphics', 'resizable', '0')
Config.set('kivy', 'keyboard_mode', 'systemanddock')

if platform == 'android':
    try:
        from android.permissions import request_permissions, Permission
        request_permissions([Permission.INTERNET])
    except Exception:
        pass

class MotorControl(BoxLayout):
    def __init__(self, **kwargs):
        super(MotorControl, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = dp(20)
        self.padding = dp(20)
        
        self.load_config()
        self.setup_ui()
        Clock.schedule_once(lambda dt: self.check_connection(), 1)
    
    def load_config(self):
        try:
            config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
            with open(config_path, 'r') as f:
                config = json.load(f)
                self.esp32_url = f"http://{config.get('esp32_ip', '192.168.1.100')}:{config.get('esp32_port', '80')}"
                self.timeout = config.get('connection_timeout', 5)
        except Exception as e:
            print(f"Error loading settings: {e}")
            self.esp32_url = "http://192.168.1.100:80"
            self.timeout = 5
    
    def setup_ui(self):
        # Application title
        self.title_label = Label(
            text='Motor Control via ESP32',
            font_size=dp(24),
            size_hint=(1, None),
            height=dp(50))
        self.add_widget(self.title_label)
        
        # Status label
        self.status_label = Label(
            text='Checking connection...',
            font_size=dp(18),
            size_hint=(1, None),
            height=dp(40))
        self.add_widget(self.status_label)
        
        # Control buttons
        buttons_layout = BoxLayout(
            orientation='horizontal',
            spacing=dp(20),
            size_hint=(1, None),
            height=dp(60))
        
        self.on_button = Button(
            text='Turn On Motor',
            font_size=dp(18),
            background_color=(0.2, 0.7, 0.2, 1))
        self.on_button.bind(on_press=self.turn_on)
        
        self.off_button = Button(
            text='Turn Off Motor',
            font_size=dp(18),
            background_color=(0.7, 0.2, 0.2, 1))
        self.off_button.bind(on_press=self.turn_off)
        
        buttons_layout.add_widget(self.on_button)
        buttons_layout.add_widget(self.off_button)
        self.add_widget(buttons_layout)
        
        # Speed control
        self.vibration_label = Label(
            text='Vibration Intensity: 50%',
            font_size=dp(16),
            size_hint=(1, None),
            height=dp(40))
        self.add_widget(self.vibration_label)
        
        self.vibration_slider = Slider(
            min=0,
            max=100,
            value=50,
            step=1,
            size_hint=(1, None),
            height=dp(50))
        self.vibration_slider.bind(value=self.on_slider_change)
        self.add_widget(self.vibration_slider)
        
        # Settings button
        self.settings_button = Button(
            text='Settings',
            font_size=dp(16),
            size_hint=(None, None),
            size=(dp(150), dp(50)),
            background_color=(0.3, 0.3, 0.7, 1))
        self.settings_button.bind(on_press=self.show_settings)
        self.settings_button.pos_hint = {'center_x': 0.5}
        self.add_widget(self.settings_button)

    def check_connection(self):
        try:
            response = requests.get(f"{self.esp32_url}/status", timeout=self.timeout)
            if response.status_code == 200:
                self.status_label.text = 'Connected'
                self.status_label.color = (0.2, 0.7, 0.2, 1)
            else:
                self.status_label.text = 'Connection Failed'
                self.status_label.color = (0.7, 0.2, 0.2, 1)
        except Exception as e:
            print(f"Error: {e}")
            self.status_label.text = 'Connection Failed'
            self.status_label.color = (0.7, 0.2, 0.2, 1)

    def turn_on(self, instance):
        try:
            response = requests.post(
                f"{self.esp32_url}/on",
                json={'speed': self.vibration_slider.value},
                timeout=self.timeout
            )
            if response.status_code == 200:
                self.show_message('Motor turned on successfully')
            else:
                self.show_message('Failed to turn on')
        except Exception as e:
            print(f"Error: {e}")
            self.show_message('Connection failed')

    def turn_off(self, instance):
        try:
            response = requests.post(f"{self.esp32_url}/off", timeout=self.timeout)
            if response.status_code == 200:
                self.show_message('Motor turned off successfully')
            else:
                self.show_message('Failed to turn off')
        except Exception as e:
            print(f"Error: {e}")
            self.show_message('Connection failed')

    def on_slider_change(self, instance, value):
        self.vibration_label.text = f'Vibration Intensity: {int(value)}%'
        try:
            requests.post(
                f"{self.esp32_url}/speed",
                json={'speed': value},
                timeout=self.timeout
            )
        except Exception as e:
            print(f"Error changing speed: {e}")

    def show_settings(self, instance):
        content = BoxLayout(orientation='vertical', padding=dp(10))
        popup = Popup(
            title='Settings',
            content=content,
            size_hint=(0.9, 0.9)
        )
        content.add_widget(Label(text=f'Device Address: {self.esp32_url}\nConnection Timeout: {self.timeout} seconds'))
        dismiss_button = Button(
            text='Close',
            size_hint=(None, None),
            size=(dp(150), dp(50)),
            pos_hint={'center_x': 0.5}
        )
        dismiss_button.bind(on_press=popup.dismiss)
        content.add_widget(dismiss_button)
        popup.open()

    def show_message(self, message):
        popup = Popup(
            title='Alert',
            content=Label(text=message),
            size_hint=(0.7, 0.3)
        )
        popup.open()
        Clock.schedule_once(popup.dismiss, 2)

class MotorControlApp(App):
    def build(self):
        return MotorControl()

if __name__ == '__main__':
    MotorControlApp().run()
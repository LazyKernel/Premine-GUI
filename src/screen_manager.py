from kivy.clock import Clock
from kivy.properties import ObjectProperty, StringProperty
from kivymd.app import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager

from log_handler import PremineLogHandler

# Screen definitions
class LogScreen(MDScreen):
    logs_text = StringProperty('')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.clock = Clock.schedule_interval(lambda dt: self.update_status(), 1)

    def update_status(self):
        logs = PremineLogHandler.get_logs_for_thread('MainThread')
        self.logs_text = '\n'.join(logs)


class MainManager(MDScreenManager):
    create_screen = ObjectProperty(None)
    status_screen = ObjectProperty(None)

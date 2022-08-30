# set default font to support japanese text
from kivy.config import Config
Config.set('kivy', 'default_font', ['NotoSansJP', 'data/NotoSansJP-Regular.otf'])

import logging
from kivymd.app import MDApp, Builder
from kivy.uix.screenmanager import NoTransition
from kivy.uix.splitter import Splitter
from kivymd.uix.boxlayout import MDBoxLayout
from screen_manager import LogScreen, MainManager
from log_handler import PremineLogHandler

# these need to be imported for builder to find classes 
# defined in kv files
from deck_create import DeckCreateScreen
from deck_status import DeckStatusScreen

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        logging.basicConfig(level=logging.DEBUG)
        root_logger = logging.getLogger()
        root_logger.addHandler(PremineLogHandler())

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Teal'

        Builder.load_file('./kv/main.kv')
        Builder.load_file('./kv/create.kv')
        Builder.load_file('./kv/status.kv')

        #splitter = Splitter(sizable_from='top')
        #splitter.add_widget(LogScreen())

        return MDBoxLayout(
            MainManager(transition=NoTransition()),
            orientation='vertical'
        )

MainApp().run()

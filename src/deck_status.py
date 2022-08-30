from kivy.clock import Clock
from kivy.properties import StringProperty
from kivymd.uix.screen import MDScreen
from deck_manager import DeckManager


class DeckStatusScreen(MDScreen):
    logs_text = StringProperty('')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.clock = Clock.schedule_interval(lambda dt: self.update_status(), 1)

    def go_back(self):
        self.clock.cancel()
        self.clock = None
        self.manager.current = 'create_screen'

    def update_status(self):
        status = DeckManager.instance().get_cur_deck_status()
        self.logs_text = status['logs']
        words_done = status['words_done']
        words_total = status['words_total']
        self.ids.words_progress_bar.value = (words_done / words_total) * 100 if words_total != 0 else 0

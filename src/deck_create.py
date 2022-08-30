from kivymd.uix.screen import MDScreen
from deck_manager import DeckManager


class DeckCreateScreen(MDScreen):
    def create_deck(self):
        deck_name = self.ids.deck_name.text
        words_str = self.ids.words_textarea.text
        words = words_str.replace('\r', '').split('\n')
        DeckManager.instance().create_deck(deck_name, words)
        self.manager.current = 'status_screen'
        

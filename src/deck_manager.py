import logging
import uuid
import threading
import inflection
from pathlib import Path
from premine.Deck import Deck
from log_handler import PremineLogHandler


class DeckManager:

    # singleton instance handling
    _instance = None

    @staticmethod
    def instance() -> 'DeckManager':
        if DeckManager._instance is None:
            DeckManager._instance = DeckManager()
        return DeckManager._instance

    # class methods
    _output_dir = './output/decks'

    def __init__(self):
        self._current_deck_id = None
        self._threads = {}
        

    def create_deck(self, name: str, words: list[str]):
        if self._current_deck_id is not None:
            logging.error('Can only have one deck in creation at a time.')
            return

        # create output dir tree if not exists
        Path(DeckManager._output_dir).mkdir(parents=True, exist_ok=True)

        deck_name_underscore = inflection.underscore(name)
        deck_id_generated = uuid.uuid4().hex
        deck = Deck()
        thread = threading.Thread(
            target=DeckManager._internal_create_deck,
            args=(deck, name, DeckManager._output_dir, deck_name_underscore, words)
        )
        thread.start()
        self._threads[deck_id_generated] = {'deck': deck, 'thread': thread}
        self._current_deck_id = deck_id_generated

    @staticmethod
    def _internal_create_deck(deck: Deck, package_name: str, package_dir: str, deck_id: str, words: list[str]):
        deck.create_deck(package_name, package_dir, deck_id, words=words)

    def get_cur_deck_status(self) -> dict:
        return self.get_deck_status(self._current_deck_id)

    def get_deck_status(self, deck_id: str) -> dict:
        if not deck_id:
            return {'logs': '', 'words_done': 0, 'words_total': 0}
        deck_info = self._threads[deck_id]
        deck = deck_info['deck']
        thread = deck_info['thread']
        logs = PremineLogHandler.get_logs_for_thread(thread.name)
        logs_str = '\n'.join(logs)
        return {'logs': logs_str, 'words_done': deck.words_done, 'words_total': deck.words_total}

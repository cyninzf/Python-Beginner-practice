# textpoker.py -- Video dice poker using a text-based interface.

from pokerapp import PokerApp
from textinterface import TextInterface

inter = TextInterface()
app = PokerApp (inter)
app.run()

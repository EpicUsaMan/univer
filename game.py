from PyQt5 import QtWidgets, QtGui, QtCore
from pyramid import Pyramid
from deck import Deck, DeckStrategy
from card import Card
import sys


class Game(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.card = False
        self._well = Deck(DeckStrategy.invisible, self)
        self._vwell = Deck(DeckStrategy.visible, self)
        self._pyramid = Pyramid(self._well, self)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtGui.QColor(3, 89, 2))
        self.setPalette(p)
        self.__score = 0

        self.score_view = QtWidgets.QLabel("Score: 0", parent=self)
        self.score_view.setGeometry(20, Card.height + 20, 200, 40)
        ps = self.score_view.palette()
        ps.setColor(self.score_view.foregroundRole(), QtGui.QColor(255, 255, 255))
        self.score_view.setPalette(ps)

        self.show()

    def cardClick(self, element: int, row: int):
        card = self._pyramid._cards[element]

        if card.leaf > 0:
            return

        if self.card == False:
            if card._rank.value == 13:
                self.score += 50
                for link in self._pyramid.getLinks(element, row):
                    link.leaf = link.leaf - 1
                card.setParent(None)
                return
            card.toggleActive()
            self.card = [card, element, row]
        else:
            if self.card[0] is card:
                card.toggleActive()
                self.card = False
                return

            if self.card[0]._rank.value + card._rank.value == 13:
                self.score += 50

                if len(self.card) == 3:
                    for link in self._pyramid.getLinks(self.card[1], self.card[2]):
                        link.leaf = link.leaf - 1

                for link in self._pyramid.getLinks(element, row):
                    link.leaf = link.leaf - 1

                self.card[0].setParent(None)
                card.setParent(None)
            else:
                self.card[0].toggleActive()
            self.card = False

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value: int):
        self.__score = value
        self.score_view.setText("Score: " + str(value))


app = QtWidgets.QApplication(sys.argv)
game = Game()
sys.exit(app.exec_())

from PyQt5 import QtWidgets, QtCore, QtGui
from deck import Deck
from card import Card


def ARF_FAC(n: int):
    if n > 1:
        return n + ARF_FAC(n - 1)
    else:
        return n


class Pyramid(QtWidgets.QFrame):
    def __init__(self, deck: Deck, parent=None):
        super().__init__(parent);

        self._cards = []
        card_width = Card.width + 20
        card_height = Card.height + 20

        self.setGeometry(card_width * 2 + 20, 20, card_width * 7, card_height * 4)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        for i in range(7):
            row_margin = self.width() - (card_width * (8 - (7 - i))) / 2 - 10
            block_margin = card_height * i
            for j in range(i + 1):
                card = deck.__next__()
                card.setParent(self)
                card.setGeometry(10 + row_margin + (card_width * j) - ((self.width() - (Card.width / 2)) / 2),
                                 10 + block_margin / 2, Card.width, Card.height)

                card.mousePressEvent = lambda event, i=i, j=j: parent.cardClick(ARF_FAC(i) + j, i + 1)
                if i == 6:
                    card.leaf = 0
                else:
                    card.leaf = 2

                card.show()

                self._cards.append(card)

        self.show()

    def getLinks(self, element: int, row: int) -> list:
        elements = ARF_FAC(row)

        if elements == element:
            return [self._cards[element - row]]
        elif elements - row == element:
            return [self._cards[element - row + 1]]
        else:
            return [self._cards[element - row + 1], self._cards[element - row]]

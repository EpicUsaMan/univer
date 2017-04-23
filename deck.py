from PyQt5 import QtWidgets, QtCore, QtGui
from card import Card, Ranks, Suits
from enum import Enum
from random import shuffle


class DeckStrategy(Enum):
    visible = 1
    invisible = 2


class Deck(QtWidgets.QStackedWidget):
    target = None

    def __init__(self, strategy: DeckStrategy, parent=None):
        super().__init__(parent=parent)
        self._strategy = strategy
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        emptyDeck = QtWidgets.QLabel()
        emptyDeck.setPixmap(QtGui.QPixmap("images/deck.png").scaled(Card.width, Card.height, QtCore.Qt.KeepAspectRatio))
        self.addWidget(emptyDeck)

        if self._strategy.value == DeckStrategy.invisible.value:
            emptyDeck.setGeometry(0, 0, Card.width, Card.height)
            self.setGeometry(20, 20, Card.width, Card.height)
            self.mousePressEvent = self.leaf
            cards = []
            for rank in Ranks:
                for suit in Suits:
                    cards.append(Card(rank, suit, parent=self))

            shuffle(cards)
            for card in cards:
                card.leaf = 2
                self.addWidget(card)

            self.setCurrentIndex(self.count() - 1)
        else:
            emptyDeck.setGeometry(10, 10, Card.width, Card.height)
            self.setGeometry(Card.width + 40, 10, Card.width + 20, Card.height + 20)
            self.mousePressEvent = self.getCard
            self.setCurrentWidget(emptyDeck)
            self.__class__.target = self

        self.show()

    def __iter__(self):
        return self

    def __next__(self):
        if self.parent().card != False and len(self.parent().card) == 1:
            self.parent().card[0].toggleActive()
            self.parent().card = False

        if self.count() > 1:
            card = self.currentWidget()
            self.removeWidget(card)
            self.setCurrentIndex(self.count() - 1)
            return card
        else:
            raise StopIteration

    def leaf(self, event):
        if self.count() > 1:
            card = self.__next__()
            card.leaf = 0
            card.setParent(self.__class__.target)
            card.setGeometry(10, 10, Card.width, Card.height)
            self.__class__.target.addWidget(card)
            self.__class__.target.setCurrentWidget(card)
        else:
            self.parent().score -= 100

            for card in self.__class__.target:
                card.leaf = 2
                card.setParent(self)
                card.setGeometry(0, 0, Card.width, Card.height)
                card.imageView()
                self.addWidget(card)
                self.setCurrentWidget(card)

    def getCard(self, event):
        card = self.currentWidget()
        if self.parent().card == False:
            if card._rank.value == 13:
                card.setParent(None)
                return
            card.toggleActive()
            self.parent().card = [card]
        else:
            if self.parent().card[0] is card:
                card.toggleActive()
                self.parent().card = False
                return

            if self.parent().card[0]._rank.value + card._rank.value == 13:
                self.parent().score += 50

                for link in self.parent()._pyramid.getLinks(self.card[1], self.card[2]):
                    link.leaf = link.leaf - 1

                self.parent().card[0].setParent(None)
                card.setParent(None)
            else:
                card.toggleActive()
            self.parent().card = False

from PyQt5 import QtWidgets, QtGui, QtCore
from enum import Enum


class Suits(Enum):
    hearts = 1
    diamonds = 2
    clubs = 3
    spades = 4


class Ranks(Enum):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13


class Card(QtWidgets.QLabel):
    width = 142 / 2
    height = 212 / 2

    def __init__(self, rank: Ranks, suit: Suits, parent=None):
        super().__init__(parent=parent)

        self._rank = rank
        self._suit = suit
        self.__leaf = 2
        self.setGeometry(0, 0, self.__class__.width, self.__class__.height)

        self.show()

    @property
    def leaf(self):
        return self.__leaf

    @leaf.setter
    def leaf(self, status: int):
        self.__leaf = status
        self.imageView()

    def imageView(self):
        if self.__leaf > 0:
            self.setPixmap(QtGui.QPixmap("images/suit.png").scaled(self.geometry().width(), self.geometry().height(),
                                                                   QtCore.Qt.KeepAspectRatio))
        else:
            self.setPixmap(QtGui.QPixmap("images/" + self._suit.name + "/" + str(self._rank.value) + ".png").scaled(
                self.geometry().width(), self.geometry().height(), QtCore.Qt.KeepAspectRatio))

    def toggleActive(self):
        if self.parent().parent().card == False:
            self.setGeometry(self.geometry().x() - 10, self.geometry().y() - 10, Card.width + 20, Card.height + 20)
        else:
            self.setGeometry(self.geometry().x() + 10, self.geometry().y() + 10, Card.width, Card.height)

        self.imageView()

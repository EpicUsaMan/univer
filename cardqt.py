# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'card.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from card import Card, Suits, Ranks

class QCard(Card, QtWidgets.QLabel):
	def __init__(self, rank, suit, visible: bool = True, parent = None):
		super().__init__(rank, suit, visible)
		super(Card, self).__init__(parent)
		self._clicked = False
		self.setGeometry(QtCore.QRect(20, 10, 93, 140))
        self.setMinimumSize(QtCore.QSize(93, 140))
        self.setMaximumSize(QtCore.QSize(142, 212))
        self.setText("")
		self.visible = visible

	def mousePressEvent(self, event):
		find = self.parent().findCard()
		if find is not None:
				self.parent().QisBeaten(find, self)
		else:
			self._clicked = True

	@property
	def visible(self) -> bool:
		return self._visible == 0

	@visible.setter
	def visible(self, state):
		if isinstance(state, int):
			self._visible = state
		elif isinstance(state, bool):
			self._visible = 0 if state else 2
		else:
			raise TypeError

		if self.visible is True:
			self.setPixmap(QtGui.QPixmap(":/"+self.suit.name+"/"+self.rank.name+".png"))
		else:
			self.setPixmap(QtGui.QPixmap(":/suit.png"))


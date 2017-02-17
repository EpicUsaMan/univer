from card import Card

class Pyramid:
	__rows = 7

	def __new__(cls):
		cls.__struct = []
		cls.__crow = 1
		return cls

	'''Adds card in a pyramid'''
	@classmethod
	def add(cls, card: Card):
		if len(cls.struct) \
		not in range(cls.__SAP(cls.__crow - 1), cls.__SAP(cls.__crow)):
			cls.__crow += 1

		if cls.__crow > cls.__rows:
			except ValueError

		card.visible = cls.__crow == 7
		self.__struct.append(card)

	@classmethod
	def __len__(cls):
		return len(cls.__struct)

	@property
	def struct(self):
		return self.__struct

	'''The sum of an arithmetic progression'''
	@staticmethod
	def __SAP(row):
		if row > 1:
			return row + ArifmeticProgressSum(row-1)
		else:
			return row

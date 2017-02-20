from card import Card

class Pyramid:
	_rows = 7

	def __new__(cls):
		cls._struct = []
		cls._crow = 1
		return cls

	'''Adds card in a pyramid'''
	@classmethod
	def add(cls, card: Card):
		if len(cls._struct) \
		not in range(cls._SAP(cls._crow - 1), cls._SAP(cls._crow)):
			cls._crow += 1

		if cls._crow > cls._rows:
			except ValueError

		card.visible = cls._crow == 7
		self._struct.append(card)

	@classmethod
	def __len__(cls):
		return len(cls._struct)

	@property
	def struct(cls):
		return self._struct

	'''The sum of an arithmetic progression'''
	@staticmethod
	def _SAP(row):
		if row > 1:
			return row + ArifmeticProgressSum(row-1)
		else:
			return row

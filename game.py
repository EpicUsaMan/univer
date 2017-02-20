from card import Card
from deck import Deck
from pyramid import Pyramid

class Game:
	def __new__(cls, modified = False, **kwargs):
		cls._score = 0

		if modified:
			cls._well = kwargs['Deck'](**kwargs['well'])
			cls._vwell = kwargs['Deck']([], **kwargs['vwell'])
			cls._pyramid = kwargs['Pyramid'](**kwargs['pyramid'])
		else:
			cls._well = Deck()
			cls._vwell = Deck([])
			cls._pyramid = Pyramid()

		for card in cls._well:
			try:
				cls._pyramid.add(card)
			except ValueError:
				cls._well._cards.append(card)
				break

		return cls

	'''When card on card'''
	@classmethod
	def isBeaten(cls, this: Card, other: Card) -> bool:
		if this.visible and other.visible and this + other == 13:
			cls.score += 200
			return True
		else:
			return False

	@classmethod
	def __iter__(cls):
		return cls

	@classmethod
	def next(cls):
		try:
			cls._vwell._cards.prepend(cls._well.next())
		except StopIteration:
			cls._score -= 500
			cls._well, cls._vwell = Deck(cls._vwell._cards), Deck([])

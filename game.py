from card import Card
from deck import Deck
from pyramid import Pyramid

class Game:
	def __new__(cls):
		cls.score = 0
		cls.well = Deck()
		cls.viewed_well = Deck([])
		cls.pyramid = Pyramid()

		for card in well:
			try:
				cls.pyramid.add(card)
			except ValueError:
				well.cards.append(card)
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
			cls.viewed_well.cards.prepend(cls.well.next())
		except StopIteration:
			cls.score -= 500
			cls.well = Deck(cls.viewed_well)
			cls.viewed_well = Deck([])


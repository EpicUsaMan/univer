from card import Card, Ranks, Suits
import random

class Deck:
	def __init__(self, cards = None):
		if cards is None:
			ranks = map(int, Ranks)
			suits = map(int, Suits)
			self._cards = []

			for rank in ranks:
				for suit in suits:
					self._cards.append(Card(rank, suit))

			def random_sort(value: Card) -> int:
				return random.randint(0, len(ranks) * len(suits)

			self._cards = self._cards.sort(key=random_sort)
		elif isinstance(cards, list) and \
			 all(isinstance(element, Card) for element in cards):
			self._cards = cards
		else:
			raise TypeError

	def __iter__(self):
		return self

	def next(self):
		if len(self._cards) > 0:
			card = self._cards[-1]
			self._cards = self._cards[:-1]
			return card
		else:
			raise StopIteration

	def current(self):
		if len(self._cards) > 0:
			return self._cards[-1]
		else:
			raise StopIteration

	def __len__(self):
		return len(self._cards)

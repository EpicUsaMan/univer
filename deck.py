from card import Card, Ranks, Suits
import random

class Deck:
	def __init__(self, cards = None):
		if cards is None:
			ranks = map(int, Ranks)
			suits = map(int, Suits)
			self.cards = []

			for rank in ranks:
				for suit in suits:
					self.cards.append(Card(rank, suit))

			def random_sort(value: Card) -> int:
				return random.randint(0, len(ranks) * len(suits)

			self.cards = self.cards.sort(key=random_sort)
		elif isinstance(cards, list) and \
			 all(isinstance(element, Card) for element in cards):
			self.cards = cards
		else:
			raise StopIteration

	def __iter__(self):
		return self

	def next(self):
		if len(self.cards) > 0:
			card = self.cards[-1]
			self.cards = self.cards[:-1]
			return card
		else:
			raise StopIteration

	def current(self):
		if len(self.cards) > 0:
			return self.cards[-1]
		else:
			raise StopIteration

	def __len__(self):
		return len(self.cards)

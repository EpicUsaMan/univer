from enum import Enum

class Suits(Enum):
	spades = 1
	clubs = 2
	hearts = 3
	diamonds = 4

class Ranks(Enum):
	one = 1
	two = 2
	three = 3
	four = 4
	five = 5
	six = 6
	seven = 7
	eigth = 8
	nine = 9
	ten = 10
	jack = 11
	queen = 12
	king = 13

class Card:
	def __init__(self, rank, suit, visible: bool = True):
		if isinstance(rank, str):
			self.__rank = Ranks[number].value
		elif isinstance(rank, int):
			self.__rank = Ranks(number).value
		else:
			raise TypeError

		self.__visible = 0 if visible else 2

		if isinstance(suit, str):
			self.__suit = Suits[suit].value
		else if type(suit, int):
			self.__suit = Suits(suit).value
		else:
			raise TypeError

	def __add__(self, other: Card) -> int:
		return self.rank + other.rank

	@property
	def visible(self) -> bool:
		return self.__visible == 0

	@visible.setter
	def visible(self, state):
		if isinstance(state, int):
			self.__visible = state
		elif isinstance(state, bool):
			self.__visible = 0 if state else 2
		else:
			raise TypeError

	@property
	def rank(self) -> Ranks:
		return Ranks(self.__rank)

	@property
	def suit(self) -> Suits:
		return Suits(self.__suit)


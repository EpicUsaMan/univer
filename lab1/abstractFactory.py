'''Define Abstract Factory'''
from abc import ABCMeta, abstractmethod

class Snack:
	pass

class Beer:
	pass

class Beer(metaclass=ABCMeta):
	@abstractmethod
	def interact(self, snack: Snack):
		pass

class Snack(metaclass=ABCMeta):
	@abstractmethod
	def interact(self, beer: Beer):
		pass

class Tuborg(Beer):
	def interact(self, snack: Snack):
		print('I buy beer {0} and {1}'.format( \
			  self.__class__.__name__, snack.__class__.__name__.lower()))

class Staropramen(Beer):
	def interact(self, snack: Snack):
		print('I buy beer {0} and {1}'.format( \
			  self.__class__.__name__, snack.__class__.__name__.lower()))

class AbstractShop(metaclass=ABCMeta):
	@abstractmethod
	def buy_beer(self) -> Beer:
		pass

	@abstractmethod
	def buy_snack(self) -> Snack:
		pass

class Peanuts(Snack):
	def interact(self, beer: Beer):
		print('I buy beer {0} and {1}'.format( \
			  beer.__class__.__name__, self.__class__.__name__.lower()))


class Chips(Snack):
	def interact(self, beer: Beer):
		print('I buy beer {0} and {1}'.format( \
			  beer.__class__.__name__, self.__class__.__name__.lower()))


class EcoMarket(AbstractShop):
	def buy_beer(self) -> Beer:
		return Tuborg()

	def buy_snack(self) -> Snack:
		return Peanuts()


class Silpo(AbstractShop):
	def buy_beer(self) -> Beer:
		return Staropramen()

	def buy_snack(self) -> Snack:
		return Chips()

'''Using AbstractFactory'''
firstShop = EcoMarket()
lastShop = Silpo()

beer = firstShop.buy_beer()
snack = lastShop.buy_snack()

snack.interact(beer)
beer.interact(snack)

beer = lastShop.buy_beer()
snack = firstShop.buy_snack()

snack.interact(beer)
beer.interact(snack)

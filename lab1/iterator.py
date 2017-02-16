'''Define Iterator'''
class Iterator:
	def __init__(self, *args):
		if len(args) == 1:
			self.__init_one(args[0])
		else:
			self.__init_more(args[0], args[1], args[2] or 1)

	def __init_one(self, maximal):
		assert isinstance(maximal, int), \
		'all arguments must be integer numbers'

		self.__min = 0
		self.__current = 0
		self.__max = maximal
		self.__step = 1

	def __init_more(self, minimal, maximal, step):
		assert step != 0, 'step must be greather or lower then 0'
		assert isinstance(minimal, int) \
		and isinstance(maximal, int) \
		and isinstance(step, int), 'all arguments must be integer numbers'

		self.__min = minimal
		self.__current = minimal
		self.__max = maximal
		self.__step = step

	def __iter__(self):
		return self

	def next(self, n = 1):
		assert isinstance(n, int), 'n must be integer number'
		assert n != 0, 'n must be greather or lower then 0'

		if (n > 0):
			if self.__current + self.__step * n <= \
			(self.__max if self.__step * n > 0 else self.__min):
				self.__current += self.__step * n
			else: raise StopIteration
		else:
			if self.__current + self.__step * n >= \
			(self.__max if self.__step * n > 0 else self.__min):
				self.__current += self.__step * n
			else: raise StopIteration

		return self.__current

'''Using Iterator'''
i = Iterator(12)
print(i.next())
print(i.next(2))
print(i.next(-2))

i = Iterator(0, 12, 2)
print(i.next())
print(i.next(2))
print(i.next(-2))

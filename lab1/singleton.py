'''Define Singleton'''
class Singleton:
	param = "ANY VALUE"

	def __new__(cls):
		cls.param = "ANY VALUE"
		return cls

'''Using Singleton'''
print(Singleton.param)
Singleton.param = "A"
print(Singleton.param)
a = Singleton()
print(a.param)

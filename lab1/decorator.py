import re
'''Define decorator'''
def wrap(tag):
	def decorate(func):
		def wrapper(*args, **kwargs):
			assert tag.startswith('<') and tag.endswith('>') and len(tag) > 2, \
			"Input valid tag"
			return (tag + "{0}" + re.sub(" .*$", "", tag.replace("<", "</"))) .format(func(*args, **kwargs))
		return wrapper

	return decorate

'''Using decorator'''
@wrap("<button>")
def image_button(inner, params):
	assert isinstance(params, dict)
	attr = []

	for key, value in params.items():
		attr.append(key+'="'+str(value)+'"')

	return "<img " + ' '.join(attr) + ">"+str(inner)

print(image_button("Text of button", {'src': 'err.png'}))

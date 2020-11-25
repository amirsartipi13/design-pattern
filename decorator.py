class WrittenText: 

	"""Represents a Written text """

	def __init__(self, text): 
		self._text = text 

	def render(self): 
		return self._text 

class UnderlineWrapper(WrittenText): 

	"""Wraps a tag in <u>"""

	def __init__(self, wrapped): 
		self._wrapped = wrapped 

	def render(self): 
		return "<u>{}</u>".format(self._wrapped.render()) 

class ItalicWrapper(WrittenText): 

	"""Wraps a tag in <i>"""

	def __init__(self, wrapped): 
		self._wrapped = wrapped 

	def render(self): 
		return "<i>{}</i>".format(self._wrapped.render()) 

class BoldWrapper(WrittenText): 

	"""Wraps a tag in <b>"""

	def __init__(self, wrapped): 
		self._wrapped = wrapped 

	def render(self): 
		return "<b>{}</b>".format(self._wrapped.render()) 

""" main method """

if __name__ == '__main__': 

	before_wrapping = WrittenText("Change text style") 
	after_wrapping = ItalicWrapper(UnderlineWrapper(BoldWrapper(before_wrapping))) 

	print("before :", before_wrapping.render()) 
	print("after :", after_wrapping.render()) 

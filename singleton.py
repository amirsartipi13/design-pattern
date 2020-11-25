# Singleton  pattern 
class Singleton: 

	# state shared by each instance 
	__shared_state = dict() 

	# constructor method 
	def __init__(self): 
		self.__dict__ = self.__shared_state 
		self.state = 'value'

	def __str__(self): 

		return self.state 

# main method 
if __name__ == "__main__": 

	singleton_1 = Singleton() # object of class Singleton 
	singleton_2 = Singleton() # object of class Singleton 
	singleton_3 = Singleton() # object of class Singleton 


	singleton_1.state = 'Value 1'    # singleton_1 changed the state 
	singleton_2.state = 'value_2'	 # singleton_2 changed the state 

	print(singleton_1) # output --> value_2 
	print(singleton_2) # output --> value_2 

	singleton_3.state = 'value_3' # singleton_3 changed the 
						        # the shared state 

	print(singleton_1) # output --> value_3 
	print(singleton_2) # output --> value_3 
	print(singleton_3) # output --> value_3 

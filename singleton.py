# Singleton  pattern 
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class TestSingleton(metaclass=Singleton): 
	# constructor method 
	def __init__(self): 
		self.value = 'value'

	def __str__(self): 
		return self.value 

# main method 
if __name__ == "__main__": 

	singleton_1 = TestSingleton() # object of class Singleton 
	singleton_2 = TestSingleton() # object of class Singleton 
	singleton_3 = TestSingleton() # object of class Singleton 

	singleton_1.value = 'Value 1'    # singleton_1 changed the Value 1 
	singleton_2.value = 'value_2'	 # singleton_2 changed the Value 2 

	print(singleton_1) # output --> value_2 
	print(singleton_2) # output --> value_2 

	singleton_3.value = 'value_3' # singleton_3 changed the value to value_3 

	print(singleton_1) # output --> value_3 
	print(singleton_2) # output --> value_3 
	print(singleton_3) # output --> value_3 

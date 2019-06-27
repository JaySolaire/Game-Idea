###I created my own vector Class!! Woop woop! Too bad I didn't use it anywhere :'(

class Vector( list ):
    def __init__(self, *data):
        self.data = data
    def __repr__(self):
        return repr(self.data) 
    def __add__(self, other):
        return list( (a+b for a,b in zip(self.data, other.data) ) )  
    def __sub__(self, other):
        return list( (a-b for a,b in zip(self.data, other.data) ) )

class FloatVector:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __repr__(self):
		return list( self.x, self.y)
	def __add__(self, other):
		return list( self.x + other.x, self.y + other.y)
	def __sub__(self, other):
		return list( self.x + other.x, self.y + other.y)

		
print(Vector(1, 2) - Vector(1, 1))


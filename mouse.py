class Pointer(object):

	def __init__(self,x,y ):
		self.x= x
		self.y= y

	def moveUp(self):
		self.y += 1
		

	def moveDown(self):
		self.y -=1
		
	def moveLeft(self):
		self.x -=1

	def moveRight(self):
		self.x +=1

	def current(self):
		print(self.x,self.y)
		print(self.x)

class Animal(object):
	def __init__(self,sound,name,age):
		self.sound=sound
		self.name=name
		self.age=age
	def eat(self,food):
		print(self.name+" is eating "+food)
	def dreaming(self,dream):
		print("the "+str(self.age)+" year old "+self.name+" is dreaming about "+dream)


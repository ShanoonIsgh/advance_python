class Person():
	def __init__(self,name = " ",age = 0):
		self.name = name
		self.age = age

	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

	def speak(self):
		print("Hello")
	def walk(self):
		print("walking away")
shanoon = Person("Sahnoon", 20)
shanoon.speak()
print(shanoon.get_name(),"is ", shanoon.get_age() )
shanoon.walk()

# First class and object

class PartyAnimal:
	x = 0

	def __init__(self):
		print("I'm contructed")

	def party(self):
		self.x = self.x +1
		print("So far", self.x)

	def __del__(self):
		print("I'm  destructed")
		pass

an = PartyAnimal()

print("Type", type(an))
print("Dir", dir(an))
#python继承

class Parent(object):

	def implicite(self):
		print("This method is only in Parent!")

	def override(self):
		print("override Now in Parent!")

	def altered(self):
		print("Parent altered()")

class Child(Parent):

	def override(self):
		print("override Now in Child")

	def altered(self):
		print("\nthis is Child")
		super(Child, self).altered()
		print("\nthis is Child")

parent = Parent()
child = Child()

parent.implicite()
child.implicite()

parent.override()
child.override()

parent.altered()
child.altered()

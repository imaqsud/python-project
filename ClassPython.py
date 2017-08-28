class Python:
    "This is first docstring of this class"

    name=""
    age=0

    def __init__(self, name, age):
        self.name=name
        self.age=age

    def display(self):
        print self.name, self.age

print Python.__doc__

pythonObject1 = Python("Mohammed", 23)

pythonObject1.display()

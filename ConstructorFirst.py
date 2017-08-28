class Constructor:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def displayData(self):
        print self.name, self.age



constructor = Constructor("Maiq", 23)

print constructor.displayData()

constructor.college = "NIT Hamirpur"

print constructor.name, constructor.age, constructor.college
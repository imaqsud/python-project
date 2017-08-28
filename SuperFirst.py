class ClassOne:

    name=""
    age=0;

    def showData(self):
        print self.name, self.age


class ClassTwo(ClassOne):

    college=""

    def showDataTwo(self):
        print self.college


classTwo = ClassTwo()

classTwo.name="Maiq"
classTwo.age=23
classTwo.college="NIT Hamirpur"

classTwo.showData()
classTwo.showDataTwo()

from xml.dom import minidom

fileTxt = open("pets.txt", "r")

pets = minidom.parseString(fileTxt.read())

fileTxt.close()

names = pets.getElementsByTagName("name")

species = pets.getElementsByTagName("species")

for name in names:
    print name.firstChild.nodeValue

for speci in species:
        print speci.firstChild.nodeValue
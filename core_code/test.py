name  = ["James", "Lianne", "Corie", "Charlotte", "Chloe"]
message =  "Hello " + name[0].title() + "."
number = len(name)
print number
name.insert(0, "Steven")
print name

def chapter_4():
    number = []
    for i in range(21):
        number.append(i)

    print number
    print min(number)
    print max(number)
    print sum(number)

    for j in name[-3:]:
        print j.title()

    Han_name = name[:]
    print "My friends are :"
    print name

    print "\n My friends are :"
    print Han_name

    print name[:3]
    print name[1:4]
    print name[-3:]

def Tuple():
    dimensions = (200, 50)
    for dimension in dimensions:
        print dimension


Tuple()

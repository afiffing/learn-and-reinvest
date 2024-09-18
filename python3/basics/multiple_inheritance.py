class Human:

    def __init__(self):
        print("Human init func")
        self.h = 'H'

    def work(self):
        print("human can work")


class Male:
    def __init__(self):
        print("Male init func")
        self.m = 'M'

    def work(self):
        print("Male can work")


# multiple inheritance  #order of inheritance matters
class Boy(Human, Male):
    def __init__(self):  # better to include all the attribute from all the classes.
        # Human.__init__(self)
        # Male.__init__(self)
        super.__init__(self)

    def work(self):
        print("Boy can work")


b1 = Boy()
b1.work()

Human.work(b1)
Male.work(b1)

# In order to check the order method resolution order is helpful mro
print(Boy.mro())  # func
# or
print(Boy.__mro__)  # field

# attributes in multiple inheritance, also human attributes will be respected
print(f'{b1.h} & {b1.m}')

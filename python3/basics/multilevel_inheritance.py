def outside_work():
    a = "Multilevel outside work func"
    print("This is the name of the namespace")
    print(__name__)
    return a


class Human:

    def __init__(self):
        print("Human init func")
        self.h = 'H'

    def eat(self):
        print("human can eat")

    def work(self):
        print("human can work")


# level1 inheritance
class Male(Human):
    def __init__(self):
        print("Male init func")
        self.m = 'M'

    def sleep(self):
        print("Male can sleep whole day")


# level2 inheritance
class Boy(Male):
    def __init__(self):
        Human.__init__(self)  # Will
        super().__init__()  # Will fetch the Male attributes

    def work(self):
        super().work()
        # or
        super(Boy, self).work()
        # or
        Human.work(self)
        print("Boy can work")

if __name__ == "__main__":
    b1 = Boy()
    b1.work()
    b1.sleep()
    b1.eat()
    print(b1.m)
    print(b1.h)

    print(__name__)

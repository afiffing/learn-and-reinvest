import multiple_inheritance
import multilevel_inheritance


# OOPs
# self int
# class/objects/attributes/methods
# Inheritance

class Instructor:
    followers = 0  # class object variable

    def __init__(self, object_name, object_address):  # init and #self
        self.name = object_name
        self.address = object_address
        # self.followers = 0

    def method_example(self, data, new_data):
        print(f'{self.name}, {self.address}, {data} and {new_data}')
        print(f'Parent class followers count is {Instructor.followers}')
        return None

    def __del__(self):
        print('Destructing the memory allocation')


class CountFollowers(Instructor):  # derived class #Inheritance
    def __init__(self, follower_name, object_name, object_address):
        super().__init__(object_name, object_address)
        # super().__init__('parent_name', 'parent_class_add')
        self.f_name = follower_name

    def update_follower(self):
        if self.f_name == 'Ashish':
            Instructor.followers += 1
        else:
            print('Incorrect follower name')
        print(f'Derived class followers count {Instructor.followers}')
        return None


if __name__ == '__main__':
    # print_hi('PyCharm')
    # r = Instructor("new data", "add complex")
    # print(r.name, r.address, r.followers)
    # print(r.method_example('data', 'new_data'))

    b = CountFollowers('Ashish', 'parent_class_name', 'parent_class_add')
    print(b.followers, b.update_follower())

    print(multilevel_inheritance.b1.work())
    print(multiple_inheritance.b1.work())

    from_module_multilevel = multilevel_inheritance.outside_work()
    print(from_module_multilevel)
    print(__name__)


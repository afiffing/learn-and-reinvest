### Pycharm help https://www.jetbrains.com/help/pycharm/getting-started.html
comment: command+'/'
run: option+r
debug: option+d

### OOPS in python https://www.youtube.com/watch?v=JeznW_7DlB0

### OOPs in python https://www.youtube.com/watch?v=Gvm2Sg1rZek

#### class and objects 
 class is a blue print
 Object is an instance of that class
 class creta(color,price,model)

 Object A = bluecreata(blue, 1400000, xyz)

 class is a user defined data type
    print(type(jenny)) - we have created a data type here
    <class '__main__.InstructorInfo'>

#### Naming convention
  Class name is PascalCase
  Method name snake_case or camelCase
  Variables snake case


#### Self and init, constructor in python
  Video: https://www.youtube.com/watch?v=G6Bd6tJ9ft0

  constructor will allow values to class method definition at the time of object instantiation

    - def _init_(self):
    - This will be called everytime an object is instantiated.

  Attributes are things an object has/have.
  Methods are task/actions that objects performs.
    a class function becomes method once it is attached to an object
    video: https://www.youtube.com/watch?v=tJNsmm7ZUmk

    class AtlassionPlayGround:
      def __init__(self, new, new2):
        self.x = new
        self.y = new2

      def display(self)  #bound to the object r below.
       ......
    if __name__ == '__main__':

        r = AtlassionPlayGround("new","new2")
        print(r.display)

### Inheritance
  derived class can access attributes and methods of parent class
  use of super() to access

  class Instructor

  class CountFollowers(Instructor)


### Multiple inheritance
  video: https://www.youtube.com/watch?v=Smlbgao6VL4

  Order of the inheritance matters
  class.MRO
  class.__mro__
  Attibutes in derived class by default is inherited from first class only.  Hence, it is better to include all the attribute from all the classes.

### Multilevel inheritance
 video: https://www.youtube.com/watch?v=Fv1xFd3LzJo
 class a --> class b --> class c

### Hierarchical inheritance
  video: https://www.youtube.com/watch?v=UYxJBJQZU-I
  class a --> class b
  class a --> class c
  class a --> class d

  same all repeated

### Hybrid
  Mix of all
  same all repeated
  Diamond problem: https://www.youtube.com/watch?v=PSMYqfMP3Cs

### Modules
 video: https://www.youtube.com/watch?v=L6BoHn8NdX4
 a py file, containing python code


### Packages
  video: https://www.youtube.com/watch?v=bcDMDlH3Vu8
  talks about 
  from package import module
  from package.sub_package import module
  use of init.py ( __all__ =["module1","module2"])

### use of __name__ == "__main__"
  video: https://www.youtube.com/watch?v=8qlf6Cg037o
  Allows single script to be executed whilte importing rest of the funcs from module.


### abstraction












### SOLID OOPS principle

https://www.youtube.com/watch?v=XI7zep97c-Y&list=PL6W8uoQQ2c61X_9e6Net0WdYZidm7zooW&index=3


DRY
Easy to maintain
Easy to understand
Flexible software
Lesser complexity


### Single responsiblity principle/min scope definition.
  - small small class with single resposibility/scope
   - small class with a single method

### Open for extension/ close for modification
  - extend small case with another method. Don't modify working method in a live class.

### Liskov substituion
    - sub/child class should extend the capability of the parent, should not narrow it down 

     parent class bike
      engine on
      accelerate 

     class motocycle  
       engine on
       accelerate + 10

      class bike
        no engine, exception "engine not present" [ functionality broken, child class narrowed the scope ]

### Interface segmented principle
   - make use of most common methods in the intefaces, avoid extra unused methods.
   similar to single responsibility for class/minimize the scope of interface.

### Dependency inversion principle

  classes depends on interfaces rather than concrete classes





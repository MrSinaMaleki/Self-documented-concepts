# Abstraction in Python

## Basics

An abstract class can be considered a **blueprint** for other classes. It allows you to create a set of methods that
must be created within any child classes built from the abstract class.

A class that contains one or more abstract methods is called an abstract class. An abstract method is a method that has
a declaration but does not have an implementation.

We use an abstract class while we are designing large functional units or when we want to provide a common interface for
different implementations of a component.

## Abstract Base Classes in Python

By defining an abstract base class, you can define a common **Application Program Interface(API)** for a set of
subclasses.
This capability is especially useful in situations where a third party is going to provide implementations, such as with
plugins, but can also help you when working in a large team or with a large code base where keeping all classes in your
mind is difficult or not possible.

## Working on Python Abstract classes

By default, Python does not provide abstract classes. Python comes with a module that provides the base for defining
**Abstract Base classes(ABC)** and that module name is ABC.

ABC works by decorating methods of the base class as an abstract and then registering concrete classes as
implementations of the abstract base. A method becomes abstract when decorated with the keyword **@abstractmethod**.

### Example 1:

```Python
from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def no_of_sides(self):
        pass


class Triangle(Polygon):
    # overriding abstract method
    def no_of_sides(self):
        print("I have 3 sides")


class Pentagon(Polygon):
    pass


my_p = Pentagon()
# results to an error because not implementing the abs method witch is 'no_of_sides'
```

### Example 2:

```Python
from abc import ABC, abstractmethod


class Animal(ABC):
    def move(self):
        pass


class Human(Animal):
    def move(self):
        print("I can walk and run. ")


class Snake(Animal):
    def move(self):
        print("I can crawl! ")


class Tree(Animal):
    pass


my_t = Tree()
# results to an error because not implementing the abs method witch is 'move'
```

## Concrete Methods in Abstract Base Classes

Concrete classes contain only concrete (normal) methods whereas abstract classes may contain both concrete methods and
abstract methods.

The concrete class provides an implementation of abstract methods, the abstract base class can also provide an
implementation by invoking the methods via super(). Let look over the example to invoke the method using super():

```Python
from abc import ABC


class R(ABC):
    def rk(self):
        print("Abstract Base Class")


class K(R):
    def rk(self):
        super().rk()
        print("subclass ")


r = K()
r.rk()
```

In the above program, we can invoke the methods in abstract classes by using super().

## Abstract Properties in Python

Abstract classes include attributes in addition to methods, you can require the attributes in concrete classes by
defining them with @abstractproperty.

```Python
from abc import ABC, abstractmethod


class Parent(ABC):
    @abc.abstractmethod
    def geeks(self):
        return "parent class"


class Child(Parent):
    @property
    def geeks(self):
        return "child class"


r = Child()
print(r.geeks)
```

## Abstract Class Instantiation

Abstract classes are incomplete because they have methods that have nobody. If Python allows creating an object for
abstract classes then using that object if anyone calls the abstract method, but there is no actual implementation to
invoke.

So, we use an abstract class as a template and according to the need, we extend it and build on it before we can use it.
Due to the fact, an abstract class is not a concrete class, it cannot be instantiated. When we create an object for the
abstract class it raises an error.

## class Examples:
Example 3:

```Python
from abc import ABC, abstractmethod


class BaseHuman(ABC):
    # instance method

    @abstractmethod
    def say_hello(self):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_id(cls):
        if cls != BaseHuman:
            raise TypeError("class method implementation error")
        raise NotImplementedError

    @property
    @abstractmethod
    def birth_date(self):
        raise NotImplementedError

    @classmethod
    @property
    @abstractmethod
    def birth_date_of_class(cls):
        raise NotImplementedError

    def get_age(self):
        return 2024 - self.birth_date


class Sina(BaseHuman):
    birth_date = 2000

    def get_id(self):
        return "id ---- "

    def thinking(self):
        print("Sina, thinking  -. -.")

    def say_hello(self):
        print("Sina, Hello !")


sina = Sina()
sina.say_hello()
```
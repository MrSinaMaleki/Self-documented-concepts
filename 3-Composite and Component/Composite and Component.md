## Composition
So far, we learned to design systems as a group of interacting objects, where each 
interaction involves viewing objects at an appropriate level of abstraction. But we 
don't know yet how to create these levels of abstraction. There are a variety of ways 
to do this; But even most design patterns rely 
on two basic object-oriented principles known as **composition** and **inheritance**. 
Composition is simpler, so let's start with it.

Composition is the act of collecting several objects together to create a new one. 
Composition is usually a good choice when one object is part of another object. 
We've already seen a first hint of composition in the mechanic example. A car is 
composed of an engine, transmission, starter, headlights, and windshield, among 
numerous other parts. The engine, in turn, is composed of pistons, a crank shaft, and 
valves. In this example, composition is a good way to provide levels of abstraction. 
The car object can provide the interface required by a driver, while also providing 
access to its component parts, which offers the deeper level of abstraction suitable 
for a mechanic. Those component parts can, of course, be further broken down if the 
mechanic needs more information to diagnose a problem or tune the engine.

This is a common introductory example of composition, but it's not overly useful 
when it comes to designing computer systems. Physical objects are easy to break 
into component objects. People have been doing this at least since the ancient Greeks 
originally postulated that atoms were the smallest units of matter (they, of course, 
didn't have access to particle accelerators). Computer systems are generally less 
complicated than physical objects, yet identifying the component objects in such 
systems does not happen as naturally.

The objects in an object-oriented system occasionally represent physical objects such 
as people, books, or telephones. More often, however, they represent abstract ideas. 
People have names, books have titles, and telephones are used to make calls. Calls, 
titles, accounts, names, appointments, and payments are not usually considered 
objects in the physical world, but they are all frequently-modeled components in 
computer systems.
#### **Composite** ---> **A way of designing a programs (when the class itself is given to the other class) If you delete the class the other one would be deleted too! So it's fair to say that their existence is relative, they are dependent to each other.**
#### **Components/Aggregation** ---> **sections of code or other objects that are given to a class**

Let's see some examples:

---

### Example 1:
```Python
class Bag:
    def __init__(self):
        self.storage = []


class Player:
    def __init__(self, name):
        self.name = name
        self.bag = Bag()  # Composite
```
In the Example above you have give a class (Bag) to The other class (Palyer)

This shows a composite relation between them.

---
Now let's take it a bit further.

```Python
# Component/Aggregation
class Game:
    def __init__(self, *players):
        self.players = players  # Component/Aggregation


fatemeh = Player("Fatemeh")  # Component
ali = Player("Ali")  # Component
reza = Player("Reza")  # Component
hamid = Player("Hamid")  # Component

my_g = Game([fatemeh, ali, reza, hamid])
```
In the example above we have give object of a class to the other class this is known as component.


Now let's change the format and give this objects to our class in the with some values in the init section:


```Python
# Composite
class Game:
    def __init__(self, player_name1, player_name2):
        self.players = [
            Player(player_name1),
            Player(player_name2)
        ]


my_g = Game("Fatemeh", "Ali")
```

---

### Example 2:
```Python
class Heart:
    def __init__(self, heartValves):
        self.heartValves = heartValves

    def display(self):
        return self.heartValves


class Person:
    def __init__(self, f_name, l_name, address, heartValves):
        self.f_name = f_name
        self.l_name = l_name
        self.address = address
        self.heartValves = heartValves  # Aggregation or Component
        self.heart = Heart  # Composition

    def display(self):
        print("First Name: ", self.f_name)
        print("Last Name: ", self.l_name)
        print("Address: ", self.address)
        print("No. of Healthy Valves: ", self.heartValves.display())


hv = Heart(4)
p = Person("Sepehr", "Emami", "555 wso blvd", hv)
p.display()
```
---
Let's reformat the code into a better one!

```Python
class Heart:
    def __init__(self, heartValves):
        self.heartValves = heartValves

    def display(self):
        return self.heartValves


class Person:
    def __init__(self, f_name, l_name, address, heartValves, count_heartvalves):
        self.f_name = f_name
        self.l_name = l_name
        self.address = address
        self.heartValves = heartValves  # Aggregation or Component
        self.heart = Heart(count_heartvalves)  # Composition

    def display(self):
        print("First Name: ", self.f_name)
        print("Last Name: ", self.l_name)
        print("Address: ", self.address)
        print("No. of Healthy Valves: ", self.heartValves.display())


hv = Heart(4)
p = Person("Sepehr", "Emami", "555 wso blvd", hv, 4)
p.display()
```

## In conclusion

* composite is just another **class** which is give to the main class in the init section, There existence is linked and you sometimes need to initiate the class in the init section of you main class as we saw in the last section of example 1.

* component is another class **instance** which is given the main class, there existence is not linked and they are not necessary related.


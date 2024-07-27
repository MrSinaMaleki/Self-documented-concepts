## This is all you need for starting your own router system.

### The whole Router Project can be separated to five different files.

---

1.      main.py
2.      routes.py

---

3.     core/state.py
4.     core/router.py
5.     core/utils.py

---

The files in core directory are essentially just static files that every standered router need.
Let's tall about them one by one.

### **3. core/state.py**

The file state.py consistes of two main classes

---

#### 1. RouteStateManager
   This class has 1 class attribute and 3 class-methods.

```Python
class RouteStateManager:
    __routes = []

    @classmethod
    def add_route(cls, route_name: str) -> None:
        if not cls.__routes:
            cls.__routes.append(route_name)
        elif cls.__routes[-1] != route_name:
            cls.__routes.append(route_name)

    @classmethod
    def get_current_route(cls) -> str:
        return "> ".join(cls.__routes)

    @classmethod
    def delete_last_route(cls):
        cls.__routes.pop()
```

---

#### 2. Auth

```Python
class Auth:
    login_status = False
```

---
You can for some menu stets and see the results by your self.

* The **add_route** is just adding some route names to the **__routes list**
* The **get_current_route method** is joining all of the elements in the list and adding a ">" between them.
* The **delete_last_route** is removing(pop()) the last index in the list.


### 5. core/utils.py
Utils.py has 3 main parts.
1. clear()
2. banner()
3. Safe()-Decorator
The first two functions are fairly simple to deal with.
The third one, on the other hand is not easy to deal with.

```Python
from os import system as terminal, name as os_name


def clear():
    terminal("cls" if os_name.lower() == "nt" else "clear")


def banner(title: str):
    clear()
    print("_"*40, f"\u001b[38;5;4m{title.title().center(40)}\u001b[0m", "="*40, sep="\n")


def safe(callback):
    def _(route):
        try:
            callback(route)
        except Exception as e:
            banner(" Error ❗ ")
            print(f"\u001b[38;5;1m{str(e)}\u001b[0m")
            if (cmd := input("\nTry Again ? [Y|n] ").strip().lower()) and cmd[0] == "n":
                route.parent()
            else:
                banner(" ⚜️ " + route.name + " ⚜️ ")
                callback(route)
    return _
```
The code above is a decorator that get's a function with a route and makes sure that the function could run properly and if there is an error it gives the user an option to start the func again or just come back and changed the banner.

You can even make a class-based decorator from the safe function.

```Python
class safe:
    def __init__(self, function):
        self.function = function

    def __call__(self, route):
        try:
            self.function(route)
        except Exception as e:
            banner(" Error ❗ ")
            print(f"\u001b[38;5;1m{str(e)}\u001b[0m")
            if (cmd := input("\nTry Again ? [Y|n] ").strip().lower()) and cmd[0] == "n":
                route.parent()
            else:
                banner(" ⚜️ " + route.name + " ⚜️ ")
                self.function(route)
```

### 4. core/router.py
core.py has 3 main parts.
1. Callback()
2. Route()
3. Router()
Each one of this has a very important task to do.
Let's talk about each one.




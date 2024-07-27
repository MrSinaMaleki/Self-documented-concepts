from importlib import import_module


class Callback:
    def __init__(self,package: str, callback: str):
        self.callback = getattr(import_module(package), callback)

    def __call__(self, *args, **kwargs):
        return self.callback(*args, **kwargs)




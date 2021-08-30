from typing import Dict, Type

from injector import Module, T, Binder, singleton

from di import Profile, Switcher


class Setter(Module):

    def __init__(self, interface: Type[T], classes: Dict[Profile, T]):
        self.__interface = interface
        self.__classes = classes

    def configure(self, binder: Binder) -> None:
        binder.bind(self.__interface, to=Switcher.get(self.__classes), scope=singleton)

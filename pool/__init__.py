import json


class Pool(object):
    def __init__(self, size):
        self.__base = dict()
        self.__size = size

    def __len__(self):
        return len(self.__base)

    def __repr__(self):
        return json.dumps(self.__base, indent=4)

    __str__ = __repr__

    @property
    def size(self):
        return self.__size

    def push(self, key, value):
        self.__base[key] = value

    def pop(self, key):
        return self.__base.pop(key, None)


def create():
    pass

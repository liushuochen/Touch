class BaseError(Exception):
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        if not self.message.startswith("."):
            self.message += "."
        return self.message

    __str__ = __repr__


class SizeLessThanZeroError(BaseError):
    def __init__(self):
        self.message = "Pool size less than zero"
        BaseError.__init__(self, self.message)

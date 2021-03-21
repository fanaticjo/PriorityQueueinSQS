from uuid import uuid1


class generator:
    def __init__(self, appender=None):
        self.appender = appender

    @property
    def generate(self):
        if self.appender is None:
            return uuid1().hex
        else:
            return f"{uuid1().hex}_{self.appender}"

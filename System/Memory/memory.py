class Memory(object):

    def __init__(self):
        self.save_vars = {}

    def save(self, variable, value):
        self.save_vars[variable] = value
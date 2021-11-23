class Memory(object):

    def __init__(self):
        self.save_vars = {}
<<<<<<< HEAD
<<<<<<< HEAD
        self.condition = None
        self.true_condition = None
        self.false_condition = None
        self.if_was = False
        self.start = False

    def save(self, variable, value):
        self.save_vars[variable] = value

    def save_condition(self, condition):
        self.condition = eval(condition)

    def append_true_commands(self, tokens):
        self.true_condition.append(tokens)

    def if_save(self, bool):
        self.if_was = bool

    def save_start(self, bool):
        self.start = bool
=======

    def save(self, variable, value):
        self.save_vars[variable] = value
>>>>>>> 078f9820365c24e2c64eb8df907b0190d0309579
=======

    def save(self, variable, value):
        self.save_vars[variable] = value
>>>>>>> 078f9820365c24e2c64eb8df907b0190d0309579

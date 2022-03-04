class TuringMachine:
    def __init__(self, tape, commands):
        self.tape = tape
        self.state = "0"
        self.commands = commands
        self.halt = False
        self.l_state = len(max(self.commands, key=len))

    def __bool__(self):
        return not self.halt

    def iterate(self):
        n_command = self.commands[self.state + self.tape.read()]
        self.state, bit, dir = n_command[:-2], n_command[-2], n_command[-1]
        self.tape.set(bit)
        if dir == "L":
            self.tape.left()
        elif dir == "R":
            self.tape.right()
        else:
            self.halt = True

    def view(self, a=-5, b=10):
        return "{}: {}".format(self.state.zfill(self.l_state),
                               self.tape.view(a, b))

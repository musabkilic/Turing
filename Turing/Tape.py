class Tape:
    def __init__(self):
        self.set_bits = set()
        self.pointer = 0

    @staticmethod
    def tape_from_view(view):
        tape = Tape()
        for i in range(len(view)):
            if view[i] == "1":
                tape.set_bits.add(i)
        return tape

    def __get(self, i):
        return str(int(i in self.set_bits))

    def read(self):
        return self.__get(self.pointer)

    def set(self, bit):
        if bit == "0":
            self.set_bits.discard(self.pointer)
        else:
            self.set_bits.add(self.pointer)

    def left(self):
        self.pointer -= 1

    def right(self):
        self.pointer += 1

    def view(self, a=-5, b=10):
        v = [self.__get(i) for i in range(a, b + 1)]
        if a <= self.pointer <= b:
            v[self.pointer - a] = "\033[4m" + v[self.pointer - a] + "\033[0m"
        return "".join(v)

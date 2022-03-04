import Turing
import time

commands = {
    "00": "00R",
    "01": "10R",
    "10": "101L",
    "11": "11R",
    "100": "110R",
    "101": "1000R",
    "110": "01H",
    "111": "111R",
    "1000": "1011L",
    "1001": "1001R",
    "1010": "101L",
    "1011": "1011L"
}
tape = Turing.Tape.tape_from_view("1111")
T = Turing.TuringMachine(tape, commands)

while T:
    time.sleep(0.2)
    print(T.view(), end="\r")
    T.iterate()

print(T.view())

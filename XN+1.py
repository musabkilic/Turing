import Turing
import time

commands = {
    "00": "00R",
    "01": "11R",
    "10": "00R",
    "11": "101R",
    "100": "110L",
    "101": "101R",
    "110": "01H",
    "111": "1000L",
    "1000": "1011L",
    "1001": "1001L",
    "1010": "1100R",
    "1011": "101R",
    "1101": "1111R",
    "1110": "111R",
    "1111": "1110R"
}
tape = Turing.Tape.tape_from_view("0100100010101011")
T = Turing.TuringMachine(tape, commands)

while T:
    time.sleep(0.2)
    print(T.view(-7, 20), end="\r")
    T.iterate()

print(T.view(-7, 20))

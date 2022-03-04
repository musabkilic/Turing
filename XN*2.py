import Turing
import time

commands = {
    "00": "00R",
    "01": "10R",
    "10": "01R",
    "11": "100R",
    "100": "111R",
    "110": "01H"
}
tape = Turing.Tape.tape_from_view("010100110")
T = Turing.TuringMachine(tape, commands)

while T:
    time.sleep(0.2)
    print(T.view(), end="\r")
    T.iterate()

print(T.view())

import Turing
import time

commands = {
    "00": "00R",
    "01": "11R",
    "10": "01H",
    "11": "11R"
}
tape = Turing.Tape.tape_from_view("0001111")
T = Turing.TuringMachine(tape, commands)

while T:
    time.sleep(0.2)
    print(T.view(), end="\r")
    T.iterate()

print(T.view())

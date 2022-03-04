import Turing
import time

commands = {
    "00": "00R",
    "01": "11L",
    "10": "101R",
    "11": "11L",
    "100": "10100R",
    "101": "110R",
    "110": "1000R",
    "111": "111R",
    "1000": "1000R",
    "1001": "1010R",
    "1010": "1110L",
    "1011": "1101L",
    "1100": "1100L",
    "1101": "11L",
    "1110": "1110L",
    "1111": "10001L",
    "10000": "10010L",
    "10001": "10001L",
    "10010": "100R",
    "10011": "11L",
    "10100": "00H",
    "10101": "10101R"
}
tape = Turing.Tape.tape_from_view("00000111111011111111")
T = Turing.TuringMachine(tape, commands)

while T:
    time.sleep(0.025)
    print(T.view(0, 20), end="\r")
    T.iterate()

print(T.view(0, 20))

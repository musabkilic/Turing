import Turing

commands = {
    "00": "00R",
    "01": "11R",
    "10": "01H",
    "11": "11R"
}
tape = Turing.Tape.tape_from_view("0001111")
T = Turing.TuringMachine(tape, commands)

while T:
    print(T.view())
    T.iterate()

print(T.view())

class Tape(object):
    blank = " "
    def __init__(self, tapeString = ""):
        self.__tape = {}
        #for i in range(len(tapeString)):
        #    self.__tape[i] = input(i)
        #hangs on input(i)
        self.__tape = dict((enumerate(tapeString)))

    def __str__(self):
        s = ""
        minIndexUsed = min(self.__tape.keys())
        maxIndexUsed = max(self.__tape.keys())
        for i in range(minIndexUsed, maxIndexUsed):
            s += self.__tape[i]
        return s

    def __getitem__(self, index):
        if index in self.__tape:
            return self.__tape[index]
        else:
            return Tape.blank

    def __setitem__(self, pos, char):
        self.__tape[pos] = char

class TuringMachine(object):
    def __init__(self, tape = "", blankSymbol = ' ', initialState = "", finalState = None, transitionFunction = None):
        self.__tape = Tape(tape)
        self.__headPosition = 0
        self.__blankSymbol = blankSymbol
        self.__currentState = initialState

        if (transitionFunction == None):
            self.__transitionFunction = {}
        else:
            self.__transitionFunction = transitionFunction

        if (finalState == None):
            self.__finalState = set()
        else:
            self.__finalState = set(finalState)

    def getTape(self):
        return str(self.__tape)
 #       return self.__tape

    def step(self):
        charUnderHead = self.__tape[self.__headPosition]
        x = (self.__currentState, charUnderHead)
        if x in self.__transitionFunction:
            y = self.__transitionFunction[x]
            self.__tape[self.__headPosition] = y[1]
            if y[2] == "L":
                self.__headPosition -= 1
            if y[2] == "R":
                self.__headPosition += 1
            self.__currentState = y[0]

    def final(self):
        if (self.__currentState in self.__finalState):
            return True
        else:
            return False


#cat files, this is the __main__ function
def main():
    initial_state = "init"
    accepting_states = ["final"]
    transition_functions = {("init", "0"):("init", "1", "R"),
                            ("init", "1"):("init", "0", "R"),
                            ("init", " "):("final", " ", "N")}
    final_states = {"final"}

    t = TuringMachine("01100 ", initialState="init", finalState = final_states, transitionFunction = transition_functions)
    print("input from tape: " + t.getTape())

    while not t.final():
        t.step()

    print("final value from tape: " + t.getTape())

main()

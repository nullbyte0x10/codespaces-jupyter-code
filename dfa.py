class DFA:
    def __init__(self, alphabet, transitions, start_state, accepting_states):
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accepting_states = accepting_states

    def accepts_language1(self, string):
        state = self.start_state
        for symbol in string:
            state = self.transitions.get((state, symbol))
            if state is None:
                return False
        return state in self.accepting_states

    def accepts_language2(self, string):
        state = self.start_state
        for symbol in string:
            state = self.transitions.get((state, symbol))
            if state is None:
                return False
            if state == 1 and symbol == 'b':
                state = 2
        return state in self.accepting_states

# Example usage for the languages "ends with aa" and "contains ab"
alphabet = {'a', 'b'}
transitions = {
    (1, 'a'): 2,
    (1, 'b'): 1,
    (2, 'a'): 3,
    (2, 'b'): 1,
    (3, 'a'): 2,
    (3, 'b'): 4,
    (4, 'a'): 4,
    (4, 'b'): 4,
}
start_state = 1
accepting_states1 = {3}
accepting_states2 = {2, 4}

# dfa = DFA(alphabet, transitions, start_state, accepting_states1)

# while True:
#     string = input("Enter a string: ")
#     if string == 'Q':
#         break
#     if dfa.accepts_language1(string):
#         print("String ends with 'aa'")
#     else:
#         print("String does not end with 'aa'")

dfa = DFA(alphabet, transitions, start_state, accepting_states2)

while True:
    string = input("Enter a string: ")
    if string == 'Q':
        break
    if dfa.accepts_language2(string):
        print("String contains 'ab'")
    else:
        print("String does not contain 'ab'")

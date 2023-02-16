# Define the DFA
def dfa(input_string):
    state = 0
    for symbol in input_string:
        if state == 0:
            if symbol == 'a':
                state = 1
            elif symbol == 'b':
                state = 3
        elif state == 1:
            if symbol == 'a':
                state = 2
            elif symbol == 'b':
                state = 3
        elif state == 2:
            if symbol == 'a':
                state = 1
            elif symbol == 'b':
                state = 3
        elif state == 3:
            if symbol == 'a':
                state = 4
            elif symbol == 'b':
                state = 3
        elif state == 4:
            if symbol == 'a':
                state = 2
            elif symbol == 'b':
                state = 3
    return state


# Prompt the user for input until Q is entered
while True:
    user_input = input("Enter a string (or Q to quit): ")
    if user_input == 'Q':
        break
    # check if the last two characters are 'aa'
    result1 = dfa(user_input[-2:]) in [2, 4]
    result2 = 'aba' in user_input  # check if the substring 'aba' is present
    if result1 and result2:
        print("The input string belongs to both languages.")
    elif result1:
        print("The input string belongs to the language that ends in aa.")
    elif result2:
        print("The input string belongs to language that contains the substring aba.")
    else:
        print("The input string does not belong to either language.")

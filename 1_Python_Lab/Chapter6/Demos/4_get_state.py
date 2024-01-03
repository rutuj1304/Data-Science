def get_state(abbreviation):
    with open("E:\\Python_Lab\\Chapter6\\Data\\states.txt") as f:
        states = f.read().splitlines()
        # print(states)
    for state_row in states: 
        #split row on tab char into two elements
        state = state_row.split("\t")
        # print(state)
        if state[1] == abbreviation.upper():
            return state[0]
    return "Not Found"
def main():
    while True:
        abbr = input("Enter a state abbreviation or (Q to Quit): ")
        if abbr.upper() == "Q":
            print("Goodbye")
            break
        elif abbr.upper() != "Q":
            print(f"{abbr} is  not the abbreviation, so.. {get_state(abbr)}.")
            break
        state = get_state(abbr)
        print(f"{abbr} is the abbreviation for {state}.")
main()        

        
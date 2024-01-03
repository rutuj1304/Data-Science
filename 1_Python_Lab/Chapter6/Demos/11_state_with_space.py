#print state names having spaces
def main():
    with open("E:\\Python_Lab\\Chapter6\\Data\\states.txt") as f:
        lines = f.read().splitlines()
    state_with_spaces = []
    for line in lines:
        state = line.split("\t")
        print(state)
        if " " in state[0]:
            state_with_spaces.append(state[0])
    for i,state_name in enumerate(state_with_spaces):
        print(f"{i+1}. {state_name}")
main()


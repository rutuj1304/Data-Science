#give numbers to the states file list using enumerate

def main():
    with open("E:\\Python_Lab\\Chapter6\\Data\\states.txt") as f:
        states = f.read().splitlines()
    for i, state in enumerate(states):
        state_name = state.split("\t")[0]
        state_abbrev = state.split("\t")[1]
        print(f"{i+1}.{state_name}  {state_abbrev}")
main()
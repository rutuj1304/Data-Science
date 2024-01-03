def main():
    phrase = input("Choose a phrase: ")
    print("Your Phrase is :",phrase)
    pos = int(input("Which character to return:[Enter a number] ")) - 1
    print("Character Number: ",pos+1,"is",phrase[pos])
main()

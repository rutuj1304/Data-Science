Black_List = [
        "Rabbani",
        "Subarao",
        "Chengappa",
        "Yelaaappa",
        "Rajesh"
]
def main():
    print("Example for loop with else")
    sentence = input("Please write a word: ")
    for i in sentence.split():
        i = i.title()
        print(i)
        if i in Black_List:
            print("You wrote black listed student. ")
            break
    else:
        print("You wrote a NON black listed student.")

    print("Example while loop with else")
    sentence = input("Please write a word: ")
    i = 0
    while i < len(sentence.split()):
        i += 1
        word = sentence.split()[i-1].title()
        print(word)
        if word in Black_List:
            print("You wrote black listed student. ")
            break
    else:
        print("You wrote a NON black listed student.")
main()
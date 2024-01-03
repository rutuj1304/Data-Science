def say_hello():
    your_name = input("What is your name? ")
    insert_seperator()
    print("Hello,",your_name,"!",sep="")

def insert_seperator():
    print("==========================")

def recite_poem():
    print("Johny Johny !")
    insert_seperator()
    print("Yes! Pappa")
    print("Eating Sugar ??")
    print("No pappa")

def say_goodbye():
    print("Goodbye!")

def main():
    say_hello()
    insert_seperator()
    recite_poem()
    insert_seperator()
    say_goodbye()
main()


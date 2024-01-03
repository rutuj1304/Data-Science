def say_hello(name):
    print("Hello,",name,"!",sep="")

def insert_seperator(s):
    print(s,s,s,sep="")

def recite_poem():
    print("Johny Johny !")
    insert_seperator("####")
    print("Yes! Pappa")
    print("Eating Sugar ??")
    print("No pappa")

def say_goodbye(name):
    print("Goodbye!",name,"!",sep="")

def main():
    your_name = input("What is your name? ")
    insert_seperator("====")
    say_hello(your_name)
    insert_seperator("----")
    recite_poem()
    insert_seperator("****")
    say_goodbye(your_name)
main()


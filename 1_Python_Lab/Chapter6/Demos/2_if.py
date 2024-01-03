def main():
    age = int(input("How old are you ? "))
    is_citizen = (input("Are you a citizen of India ? Y or N  ").lower()=='y')
    if age >= 21 and is_citizen: print("You can vote and drink")
    elif(age >= 21 and not is_citizen): print("You can drink, but can not vote")
    elif(age >= 18 and is_citizen): print("You can vote, but can not drink")
    else: print("You can not vote and drink")
main()



def main():
    total = 0
    while True:
        try:
            num = input("Enter a number: ")
            if num.lower() == 'q':
                print("Goodbye")
                break
            num = int(num) #this might cause an error
            
        except ValueError:
            print("Please enter integers only")
        else:
            total += num
            print("The Current Total is:",total)
main()
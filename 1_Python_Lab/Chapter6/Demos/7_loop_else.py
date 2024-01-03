def main():
    print("Example 1: For loop")
    num = int(input("Enter a number: "))
    for i in range(9):
        if i==num:
            break
        print(i)
    else:
        print(f"Completed iterating without reaching {num}")

    print("Example 2: While loop")
    num = int(input("Enter a number: "))
    i = 0
    while i<9:
        if i==num:
            break
        print(i)
        i+=1
    else:
        print(f"Completed iterating without reaching {num}")
    


main()
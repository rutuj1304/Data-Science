def divide():
    try:
        numerator = int(input("Enter numerator: "))
        denominator = int(input("Enter denominator: "))
        result = numerator / denominator
        print(f"{numerator} / {denominator} = {result}")
    except ValueError:
        print("Please enter a numeric value")
        divide()
    except ZeroDivisionError:
        print("You can't divide by zero! ")
        divide()
    except KeyboardInterrupt:
        print("Quitter !")
    except:
        print("I have no idea, what went wrong ! ")
def main():
    divide()
main()
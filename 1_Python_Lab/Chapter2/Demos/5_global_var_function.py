x = 0

def set_x():
    global x
    x = 1
    print("from set_x(): x =",x)

def get_x():
    print("from get_x(): x =",x)
    
def main():
    set_x()
    get_x() 

main()
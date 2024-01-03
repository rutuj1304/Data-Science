def add_numbers(num,*nums):
    total = sum(nums,num)
    print(f"The sum of {nums} and {num} is : {total} ")

def main():
    num = int(input("Enter a number : "))
    add_numbers(num,100)
    add_numbers(num,1,2,3,4,5,6,7,8,9,10)
main()


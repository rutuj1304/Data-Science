"""
Up to Rs. 3 lakh - 0% (Nil)
Rs. 3lakh to 6 lakh - 5%
Rs. 6lakh to Rs. 12 lakh - 15%
Rs 12lakh to Rs 15lakh - 20%
above Rs 15lakh - 30%

take input from user : ask him to enter income
and calculate and print : Income Tax
"""

income = float(input("Enter your income : "))

if income <= 300000:
    print("Your tax is : ", income * 0 / 100)
elif income>300000 and income <= 600000:
    print("Your tax is : ", income * 5 / 100)
elif income>600000 and income <= 1200000:
    print("Your tax is : ", income * 15 / 100)
elif income>1200000 and income <= 1500000:
    print("Your tax is : ", income * 20 / 100)
else:
    print("Your tax is : ", income * 30 / 100)

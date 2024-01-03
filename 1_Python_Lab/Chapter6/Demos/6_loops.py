#while loop
print("=======================While Loop=====================")
num = 0
while num < 6:
    print(num)
    num+=1

#for loop
print("======================for loop=======================")
print("--------------Example 1")
for num in range(6):print(num)

print("---------------Example 2")
for num in range(5,10):print(num)

print("---------------Example 3")
for num in range(11,20,2):print(num)

print("---------------Example 4")
for num in range(50,40,-1):print(num)

print("---------------Example 5")
nums = [10,20,30,40,50]
for num in nums:print(num)

print("---------------Example 6")
nums = 10,20,30,40,50
for num in nums:print(num)

print("---------------Example 7")
grades = {
    "English":97,
    "Math" : 81,
    "Biology":86
}
for i in grades:print(i)

for i in grades.keys():print(i)

for i in grades.values():print(i)

for i,j in grades.items():print(f"{i} : {j}")

for i in grades.items():
    course = i[0]
    grade = i[1]
    print(f"{course} : {grade}")

print("---------------Example 8")
for i in range(11,20):
    print(i)
    if (i % 5 == 0):break

print("---------------Example 8")
for i in range(11,20):
    if (i % 5 == 0):continue
    print(i)













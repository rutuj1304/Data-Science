import random 

#random number between 0 and 1
print(random.random())
print(random.random())
print(random.random())

print("======================")
#random int between and including a and b
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))

print("======================")

#random float between and including a and b

print(random.uniform(1,10))
print(random.uniform(1,10))
print(random.uniform(1,10))

print("======================")

#random int between 0 and b-1
print(random.randrange(10))

#random int between a and b-1
print(random.randrange(1,10))

#random int at step between a and b-1
print(random.randrange(1,10,2))



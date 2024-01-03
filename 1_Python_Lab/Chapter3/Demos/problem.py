"""
1) pizza
    how many guest are eating 
    how many slices per person
    how many slices per pie
how many pizza requires
    how many slices - leftover
pizza = 6 slices
people = 15
"""
import math
total_people = int(input("No. people: "))
slices_per_pizza = int(input("Slices per pizza: "))

total_slices_needed = total_people * slices_per_pizza
print("Total slices needed: ", total_slices_needed)

slice_per_pie = int(input("Slice per pie: "))

pizza_required = math.ceil(total_slices_needed / slice_per_pie)
print("Total pizza required: ",pizza_required)


leftover_slices = (pizza_required * slice_per_pie) - total_slices_needed
print("Leftover slices:",leftover_slices)




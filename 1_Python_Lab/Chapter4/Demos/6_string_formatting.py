#string formatting using format function
sentence = "On scale of {0:d} to {1:d}, I give {2:s} a {3:d}"
sentence = sentence.format(1, 10, "Monty Python", 6)
print(sentence)

#string formatting using % symbol
sentence = "On scale of %d to %d, I give %s a %d"
sentence = sentence % (1, 10, "Monty Python", 6)
print(sentence)


sentence = "On scale of {:d} to {:d}, I give {:s} a {:d}"
sentence = sentence.format(1, 10, "Monty Python", 6)
print(sentence)

sentence = "On scale of {:} to {:}, I give {:} a {:}"
sentence = sentence.format(1, 10, "Monty Python", 6)
print(sentence)

sentence = "On scale of {} to {}, I give {} a {}"
sentence = sentence.format(1, 10, "Monty Python", 6)
print(sentence)

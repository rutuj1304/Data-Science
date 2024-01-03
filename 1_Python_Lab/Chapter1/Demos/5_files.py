with open("E:\\Python_Lab\\Chapter1\\Data\\1880-boys.txt") as f_boys:
    boys = f_boys.read()

with open("E:\\Python_Lab\\Chapter1\\Data\\1880-girls.txt") as f_girls:
    girls = f_girls.read()

b = open("E:\\Python_Lab\\Chapter1\\Data\\1880-all.txt","w")
b.write(boys + "\n" + girls)
b.close()

a = open("../chapter1/data/1880-boys.txt")
for i  in a: print(i)

    


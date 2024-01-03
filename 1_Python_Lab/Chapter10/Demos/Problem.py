"""
1)Take input from users 6 subjects and their marks
2) calculate total and average of marks
3)Assign grade based on average
    A+ ---- >=90 to 100
    B+ --- >=75 to <90
    C+ --- >=60 to <75
    Fail --- <60
"""
def avg_fun(marks):
    return sum(marks)/len(marks)

def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75 and avg < 90:
        return "B+"
    elif avg >= 60 and avg < 75:
        return "C+"
    else:
        return "Fail"

marks = []
subjects = []
sub_mark_list = {}
for i in range(6):
    marks.append(int(input("Enter marks: ")))
    subjects.append(input("Enter Subjects: "))
    sub_mark_list[subjects[i]] = marks[i]

print(sub_mark_list)
avg = avg_fun(marks)
print(f"Total Marks Obtained: {sum(marks)}")
print(f"Average is: {avg}")
print(f"Grade is: {grade(avg)}")

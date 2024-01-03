def main():
    grades = {}
    grades["English"] = int(input("Enter grades for english: "))
    grades["Math"] = int(input("Enter grades for Math: "))
    grades["Biology"] = int(input("Enter grades for Biology: "))
    grades["Physics"] = int(input("Enter grades for Physics: "))
    grades["Hindi"] = int(input("Enter grades for Hindi: "))
    grades["Chemistry"] = int(input("Enter grades for Chemistry: "))
    
    gradepoints = grades.values()
    average = calAvg(gradepoints)
    print("Your Average Is: ",average)

def calAvg(gp):
    average = sum(gp)/len(gp)
    return average

main()


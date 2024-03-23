# Grade Analyzer

def average_grade(grades):
    return sum(grades) / len(grades)

def highest_grade(grades):
    return max(grades)

def lowest_grade(grades):
    return min(grades)

def categorize_grades(grades):
    for grade in grades:
        if grade >= 90:
            print("A")
        elif grade >= 80:
            print("B")
        elif grade >= 70:
            print("C")
        elif grade >= 60:
            print("D")
        else:
            print("F")
            
random_grades = [80, 74, 90, 60, 45, 100, 85, 92, 78, 88]

print(average_grade(random_grades))
print(highest_grade(random_grades))
print(lowest_grade(random_grades))
categorize_grades(random_grades)

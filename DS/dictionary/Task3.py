def get_grade(marks):
    if marks > 85:
        return "A+"
    elif marks > 80:
        return "A"
    elif marks >= 75:
        return "B+"
    else:
        return "Below B+"

result = {
    "Standard 1": {
        "Maths": {"Marks": 90, "Grade": "A+"},
        "English": {"Marks": 85, "Grade": "A"},
        "Art": {"Marks": 100, "Grade": "A+"},
        "EVS": {"Marks": 75, "Grade": "B+"},
        "Sports": {"Marks": 85, "Grade": "A"},
        "Hindi": {"Marks": 80, "Grade": "A"},
        "Total" : 515
    },
    "Standard 2": {
        "Maths": {"Marks": 95, "Grade": "A+"},
        "English": {"Marks": 95, "Grade": "A+"},
        "Art": {"Marks": 100, "Grade": "A+"},
        "EVS": {"Marks": 70, "Grade": "Below B+"},
        "Sports": {"Marks": 80, "Grade": "A"},
        "Hindi": {"Marks": 90, "Grade": "A+"},
        "Total" : 530
    },
    "Standard 3": {
        "Maths": {"Marks": 100, "Grade": "A+"},
        "English": {"Marks": 90, "Grade": "A+"},
        "Art": {"Marks": 90, "Grade": "A+"},
        "EVS": {"Marks": 85, "Grade": "A"},
        "Sports": {"Marks": 90, "Grade": "A+"},
        "Hindi": {"Marks": 85, "Grade": "A"}
    },
    "Standard 4": {
        "Maths": {"Marks": 90, "Grade": "A+"},
        "English": {"Marks": 85, "Grade": "A"},
        "Art": {"Marks": 85, "Grade": "A"},
        "EVS": {"Marks": 90, "Grade": "A+"},
        "Sports": {"Marks": 95, "Grade": "A+"},
        "Hindi": {"Marks": 95, "Grade": "A+"}
    },
    "Standard 5": {
        "Maths": {"Marks": 95, "Grade": "A+"},
        "English": {"Marks": 95, "Grade": "A+"},
        "Art": {"Marks": 80, "Grade": "A"},
        "EVS": {"Marks": 80, "Grade": "A"},
        "Sports": {"Marks": 100, "Grade": "A+"},
        "Hindi": {"Marks": 80, "Grade": "A"},
        "Dance": {"Marks": 85, "Grade": "A"}
    },
    "Standard 6": {
        "Maths": {"Marks": 90, "Grade": "A+"},
        "English": {"Marks": 85, "Grade": "A"},
        "Art": {"Marks": 85, "Grade": "A"},
        "Science": {"Marks": 90, "Grade": "A+"},
        "Sports": {"Marks": 95, "Grade": "A+"},
        "Hindi": {"Marks": 100, "Grade": "A+"},
        "Dance": {"Marks": 85, "Grade": "A"}
    },
    "Standard 7": {
        "Maths": {"Marks": 100, "Grade": "A+"},
        "English": {"Marks": 90, "Grade": "A+"},
        "Art": {"Marks": 75, "Grade": "B+"},
        "Science": {"Marks": 80, "Grade": "A"},
        "Sports": {"Marks": 85, "Grade": "A"},
        "Hindi": {"Marks": 85, "Grade": "A"},
        "Dance": {"Marks": 90, "Grade": "A+"}
    },
    "Standard 8": {
        "Maths": {"Marks": 85, "Grade": "A"},
        "English": {"Marks": 80, "Grade": "A"},
        "Art": {"Marks": 90, "Grade": "A+"},
        "Science": {"Marks": 90, "Grade": "A+"},
        "Sports": {"Marks": 95, "Grade": "A+"},
        "Hindi": {"Marks": 80, "Grade": "A"},
        "Dance": {"Marks": 100, "Grade": "A+"},
        "Music": {"Marks": 90, "Grade": "A+"}
    },
    "Standard 9": {
        "Maths": {"Marks": 90, "Grade": "A+"},
        "English": {"Marks": 90, "Grade": "A+"},
        "Art": {"Marks": 80, "Grade": "A"},
        "Science": {"Marks": 85, "Grade": "A"},
        "Sports": {"Marks": 90, "Grade": "A+"},
        "Hindi": {"Marks": 95, "Grade": "A+"},
        "Dance": {"Marks": 90, "Grade": "A+"},
        "Music": {"Marks": 80, "Grade": "A"}
    },
    "Standard 10": {
        "Maths": {"Marks": 85, "Grade": "A"},
        "English": {"Marks": 80, "Grade": "A"},
        "Art": {"Marks": 90, "Grade": "A+"},
        "Science": {"Marks": 90, "Grade": "A+"},
        "Sports": {"Marks": 95, "Grade": "A+"},
        "Hindi": {"Marks": 80, "Grade": "A"},
        "Dance": {"Marks": 100, "Grade": "A+"},
        "Music": {"Marks": 90, "Grade": "A+"}
    },
    "Standard 11": {
        "Mathematics": {"Marks": 85, "Grade": "A"},
        "Physics": {"Marks": 80, "Grade": "A"},
        "Chemistry": {"Marks": 90, "Grade": "A+"},
        "English": {"Marks": 80, "Grade": "A"},
        "Hindi": {"Marks": 85, "Grade": "A"},
        "CS": {"Marks": 100, "Grade": "A+"}
    },
    "Standard 12": {
        "Mathematics": {"Marks": 90, "Grade": "A+"},
        "Physics": {"Marks": 85, "Grade": "A"},
        "Chemistry": {"Marks": 80, "Grade": "A"},
        "English": {"Marks": 80, "Grade": "A"},
        "Hindi": {"Marks": 80, "Grade": "A"},
        "CS": {"Marks": 100, "Grade": "A+"}
    }
}

for std, scorecard in result.items():
    print(std ) 
    for sub,marks in scorecard.items():
        print(f"Subject = {sub}, Marks = {marks}")
    
    print()  
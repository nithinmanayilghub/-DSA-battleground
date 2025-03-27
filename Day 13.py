############################################ DAY 13##########################################################
## Question 23: Nested List + Nested Dictionary + Comprehension
###You're given a nested list of dictionaries,
### where each dictionary represents a student's performance in multiple subjects across multiple semesters.
### Write a code that calculates the total marks in all semesters only for those students who scored more than 80 in every subject of every semester.
### Input:
students = [
    {
        "name": "Amit",
        "semesters": [
            {"Math": 88, "Science": 91, "English": 85},
            {"Math": 90, "Science": 92, "English": 84},
        ],
    },
    {
        "name": "Pooja",
        "semesters": [
            {"Math": 79, "Science": 95, "English": 88},
            {"Math": 82, "Science": 81, "English": 85},
        ],
    },
    {
        "name": "Ravi",
        "semesters": [
            {"Math": 87, "Science": 88, "English": 89},
            {"Math": 91, "Science": 90, "English": 93},
        ],
    },
]
# Expected Output:
# {'Amit': 530, 'Ravi': 539}


##### ANSWER
def total_marks(students):
    # Initialize an empty dictionary
    result = {}
    # Start a loop for extracting required elements
    for student in students:
        # extract name and store it in a variable called names
        name = student["name"]
        # extract semesters and store it in a varaible called semesters
        semesters = student["semesters"]
        # check if the marks obtained by the student inall semesters is greater than 80
        if all(
            all(score > 80 for score in semester.values()) for semester in semesters
        ):
            # calculate the summ of marks
            total_marks = sum(
                [sum(marks for marks in semester.values()) for semester in semesters]
            )
            # store corresponding total marks of each student in a dictionary
            result[name] = total_marks
    # return results
    return result


print(total_marks(students))

##########################################################################################################################################################
## You’re given a nested list where each element represents a city.
## Each city contains areas, and each area has a list of temperature readings for the past 7 days.
##Find the city name(s) where all areas had an average temperature above 30°C over the week. Return a list of such city names using nested list and dictionary comprehension.
### Input:
cities = [
    {
        "name": "Mumbai",
        "areas": {
            "Andheri": [32, 33, 31, 30, 29, 34, 35],
            "Bandra": [31, 32, 30, 30, 31, 33, 34],
        },
    },
    {
        "name": "Delhi",
        "areas": {
            "Rohini": [28, 29, 27, 30, 31, 32, 29],
            "Saket": [33, 35, 36, 34, 33, 32, 31],
        },
    },
    {
        "name": "Chennai",
        "areas": {
            "T Nagar": [34, 35, 36, 37, 34, 35, 33],
            "Velachery": [32, 31, 33, 34, 32, 30, 31],
        },
    },
]
# Expected Output:
# ['Chennai']


def city_above_thirty(cities):
    results = [
        city["name"]
        for city in cities
        if all(sum(temp) / len(temp) > 30 for temp in city["areas"].values())
    ]
    return results


print(city_above_thirty(cities))

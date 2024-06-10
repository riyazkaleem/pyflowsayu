#implementation of basic dictionary
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}

for student in student_scores:
  if student_scores[student] >= 91 and student_scores[student] <= 100:
    student_grades[student] = "Outstanding"
  elif student_scores[student] >= 81 and student_scores[student] <= 90:
    student_grades[student] = "Exceeds Expectations"
  elif student_scores[student] >= 71 and student_scores[student] <= 80:
    student_grades[student] = "Acceptable"
  elif student_scores[student] <= 70:
    student_grades[student] = "Fail"

print(student_grades)

#implementation of nesting in dictionary
country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

def add_new_country(country, visits, list_of_cities):
  travel_dict = {
    "country": country,
    "visits": visits,
    "cities": list_of_cities
  }
  travel_log.append(travel_dict)

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
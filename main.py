from cv_generator import contact_details, technical_skills
from cv_generator import  cv_title
from cv_generator import collect_trainings
from cv_generator import  collect_experiences
from cv_generator import professionnal_skills
from cv_generator import personal_project
from cv_generator import  collect_projects



#display data
""" 
contact = contact_details()
print(contact["first_name"])
print(contact["last_name"])
print(contact["phone"])

print(contact["email"])
print(contact["residence"])
print(contact["mention"])


cv = cv_title()
print(cv["title"])

training= collect_trainings()

for i, trn in enumerate(training, 1 ):
    print(f"Formation {i}")

    print(trn["title"])
    print(trn["school"])
    print(trn["date_start"])
    print(trn["date_end"])
"""
""" 
experience = collect_experiences()
for i, exp in enumerate(experience, 1):
    print(f"Experience professionnelle {i}")

    print(exp["title"])
    print(exp["company"])
    print(exp["date_start"])
    print(exp["date_end"])
    print(exp["summary"])
"""

#tech_skills= technical_skills()
#print(tech_skills)

#pro_skills = professionnal_skills()
#print(pro_skills)


""" 
projects= collect_projects()
for i, prj in enumerate(projects, 1):
    print(f"Projet personnel {i}")

    print(prj["title"])
    print(prj["summary"])
    print(prj["link"])

"""

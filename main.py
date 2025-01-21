from cv_generator import contact_details, technical_skills
from cv_generator import  cv_title
from cv_generator import collect_trainings
from cv_generator import  collect_experiences
from cv_generator import professionnal_skills
from cv_generator import  technical_skills
from cv_generator import personal_project
from cv_generator import  collect_projects
from file_generator import create_file
from file_generator import  save_file
from file_generator import  header_cv
from file_generator import training_part
from file_generator import pro_experiences_part
from file_generator import  tech_skills
from file_generator import pro_skills
from file_generator import perso_projects
from file_generator import file_name

try :
    #create new file
    cv= create_file()
except Exception as E :
    print(f"Error: {E}")


#contact details
contact = contact_details()

#title of CV
title_cv= cv_title()
 
#header cv
header= header_cv(cv, contact,title_cv)


#trainings part
trn_list= collect_trainings()
training_part(cv, trn_list)

#professionnal experiences part
experiences= collect_experiences()
pro_experiences_part(cv, experiences)

#technical skills part
tch_skills= technical_skills()
tech_skills(cv, tch_skills)

#professionnal skills
prf_skills = professionnal_skills()
pro_skills(cv,prf_skills)


#personal project part
prj_perso = collect_projects()
perso_projects(cv, prj_perso)

#file name
name_file = file_name()

#save file


try :
    save_file(cv,name_file)
except Exception as E :
    print(f"Error: {E}")
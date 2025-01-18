import re
from itertools import count

from functions import  valided_names
from functions import valided_date
from functions import valided_email
from functions import compare_dates


#contact_details
def contact_details():

    #first_name
    while True:
        first_name=input("Saisir votre prénom :").strip()
        if not first_name or not valided_names(first_name):
            print("Saisie incorrecte!")
        else:
            break

    #last_name
    while True:
        last_name= input("Saisir votre nom de famille : ").strip()
        if not last_name or not valided_names(last_name):
             print("Saisie incorrecte!")
        else:
            break

    #phone
    while True:
        phone= input("Saisir votre numéro de téléphone :").strip()
        if not phone or not phone.isdigit():
            print("Saisie incorrecte!")
        else:
            break

    #email
    while True:
        email = input("Saisir votre email :").strip()
        if not email or not valided_email(email):
            print("Saisie incorrecte!")
        else:
            break

    #residence
    while True:
        residence= input("Saisir votre lieux de residence : ").strip()
        if not residence or not residence.isalpha():
            print("Saisie incorrecte!")
        else:
            break

    #mention
    while True:
        mention = input("Saisir une mention si necessaire : ").strip()
        if not mention.isalpha():
            print("Saisie incorrecte!")
        else:
            break

    return {
        "first_name": first_name,
        "last_name":  last_name,
        "phone": phone,
        "email": email,
        "residence": residence,
        "mention": mention
    }

#title of the CV
def cv_title():

    #title
    while True:
        title= input("Saisir le titre du CV : ").strip()
        if not title:
            print("Saisie incorrecte!")
        else:
            break

    return {
        "cv_title": title
    }

#trainings
def trainings():

    #training's title
    while True:
        trn_title= input("Saisir un titre de formation : ").strip()
        if not trn_title:
            print("Saisie incorrecte!")
        else:
            break
    #training's school
    while True:
        trn_school = input("Saisir le nom de l'établissement de formation :  : ")
        if not trn_school:
            print("Saisie incorrecte!")
        else:
            break

    #dates part
    while True:
        #training's date start
        while True:
            trn_start= input("Saisir la date  de début de formation : ")
            if  not trn_start or not valided_date(trn_start):
                print("Saisie incorrecte!")
            else:
                break

        #training's date end
        while True:
            trn_end = input("Saisir la date de fin de formation : ")
            if not trn_end or not valided_date(trn_end):
                print("Saisie incorrecte!")
            else:
                break
        #error handling for dates
        if not compare_dates(trn_start, trn_end):
            print("Saisie incorrecte, la date de fin de formation ne peut pas être inférieur à la date de début! ")
        else:
            break

    return {
         "title": trn_title,
        "school": trn_school,
        "date_start": trn_start,
        "date_end": trn_end
    }


#collect_trainings
def collect_trainings():
    trainings_list = []
    count = 0

    while count < 3:
        print(f"Formation {count+1}")
        new_training = trainings()
        trainings_list.append(new_training)

        if count < 2 :
            while True:
                more = input("Voulez-vous entrer une autre formation ? oui / non : ").strip().lower()
                if more == "oui":
                    break
                elif more == "non":
                    return trainings_list
                else:
                    print("Saisie incorrecte ! Tapez : oui ou non : ")
        count+=1

    return trainings_list



#professional experiences
def professional_experiences():

    # title
    while True:
        exp_title = input("Saisir le titre de l'expérience professionnelle : ").strip()
        if not exp_title:
            print("Saisie incorrecte!")
        else:
            break

    # company
    while True:
        exp_company = input("Saisir l'entreprise : ").strip()
        if not exp_company:
            print("Saisie incorrecte!")
        else:
            break

    # dates part
    while True:

        # date start
        while True:
            exp_start = input("Saisir le début de l'expérience professionnelle : ")
            if not exp_start or not valided_date(exp_start):
                print("Saisie incorrecte!")
            else:
                break

        # date end
        while True:
            exp_end = input("Saisir la fin de l'expérience professionnelle : ")
            if not exp_end or not valided_date(exp_end):
                print("Saisie incorrecte!")
            else:
                break

        # error handling dates
        if not compare_dates(exp_start, exp_end):
            print("Saisie incorrecte, la date de fin d'expérience professionnelle ne peut pas être inférieur à la date de début!")
        else:
            break

    # summary
    while True:
        exp_summary = input("Saisir un résumé de votre expérience professionnelle : ").strip()
        if not exp_summary:
            print("Saisie incorrecte!")
        else:
            break

    return {
        "title": exp_title,
        "company": exp_company,
        "date_start": exp_start,
        "date_end": exp_end,
        "summary": exp_summary
    }



#collect professional experiences
def collect_experiences():
    experiences_list = []
    count= 0

    while count < 3 :
        print(f"Expériences professionnelles {count+1}")
        new_experience= professional_experiences()
        experiences_list.append(new_experience)

        while True:
            more = input("Voulez-vous entrer une autre expérience professionnelle ? tapez oui / non :").strip().lower()
            if more == "oui":
                count+=1
                break
            elif more == "non":
                return experiences_list
            else:
                print("Saisie incorrecte! tapez oui / non : ")

    return  experiences_list

#technical skills
def technical_skills():
    while True:
        skills= input("Saisir vos compétences techiques, chaque compétences doit être séparée par une virgule : ").strip()
        if not skills:
            print("Saisie incorrecte!")
        else:
            break

    return skills

#professionnal skills
def professionnal_skills():
    while True:
        pro_skills= input("Saisir vos compétences professionnelles séparées par une virgule : ")
        if not pro_skills:
            print("Saisie incorrecte!")
        else:
            break

    return pro_skills

#personal projects
def personal_project():

    #title
    while True:
        project_title= input("Saisir le titre du projet personnel : ").strip()
        if not project_title:
            print("Saisie incorrecte!")
        else:
            break

    #summary
    while True:
        project_summary = input("Saisir une explication de votre projet : ").strip()
        if not project_summary:
            print("Saisie incorrecte!")
        else:
            break

    #link
    while True:
        project_link= input("Saisir un lien vers votre projet comme une URL : ")
        if not project_link or project_link:
            break

    return {
        "title": project_title,
        "summary": project_summary,
        "link": project_link
    }


#collect projects
def collect_projects():
    projects_list = []
    count = 0

    while count < 3:
        print(f"Projet personnel {count + 1}")

        new_project = personal_project()
        projects_list.append(new_project)

        if count < 2:
            while True:
                more = input("Voulez-vous ajouter un projet personnel? tapez oui / non : ").strip().lower()
                if more == "oui":
                    break
                elif more == "non":
                    return projects_list
                else:
                    print("Saisie incorrecte! tapez oui / non : ")
        count += 1

    return projects_list

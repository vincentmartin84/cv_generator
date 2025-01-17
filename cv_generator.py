import re
from itertools import count

from functions import valided_names, valided_email, valided_date, compare_dates


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

        while True:
            more = input("Voulez-vous entrer une autre formation ? oui / non : ").strip().lower()
            if more == "oui":
                count += 1
                break  # Sort de la boucle pour ajouter une nouvelle formation
            elif more == "non":
                return trainings_list  # Retourne la liste des formations et arrête la collecte
            else:
                print("Saisie incorrecte ! Tapez : oui ou non : ")

    return trainings_list  # Retourne la liste si on atteint la limite de 3 formations



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


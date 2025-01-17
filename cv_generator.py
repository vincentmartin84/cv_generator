import re

#contact_details
def contact_details():

    #first_name
    while True:
        first_name=input("Saisir votre prénom :").strip()
        if not first_name or not first_name.isalpha():
            print("Saisie incorrecte!")
        else:
            break

    #last_name
    while True:
        last_name= input("Saisir votre nom de famille : ").strip()
        if not last_name or not last_name.isalpha():
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
    regex_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    while True:
        email = input("Saisir votre email :").strip()
        if not email or not re.match(regex_email, email):
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
            trn_start= int(input("Saisir une année de début de formation : "))
            if  not trn_start:
                print("Saisie incorrecte!")
            else:
                break

        #training's date end
        while True:
            trn_end = int(input("Saisir une année de fin de formation : "))
            if not trn_end:
                print("Saisie incorrecte!")
            else:
                break
        #error handling for dates
        if not trn_start < trn_end :
            print("Saisie incorrecte, la date de fin de formation ne peut pas être supérieur à la date de début! ")
        else:
            break

    return {
         "title": trn_title,
        "school": trn_school,
        "date_start": trn_start,
        "date_end": trn_end
    }







#display datas
#contact= contact_details()
#title_cv = cv_title()
training = trainings()


""" 
print(contact["first_name"])
print(contact["last_name"])
print(contact["phone"])
print(contact["email"])
print(contact["residence"])
print(contact["mention"])
"""


print(training["title"])
print(training["school"])
print(training["date_start"])
print(training["date_end"])

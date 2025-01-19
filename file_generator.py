from docx import  Document

#create new file
def create_file():
    cv_doc = Document()
    return cv_doc

#save the file
def save_file(document, name_file):
    document.save(name_file )


#create header Cv
def header_cv(document, contact, title):

    table = document.add_table(rows=1, cols=2)
    cell_contact= table.cell(0,0)
    cell_title= table.cell(0,1)

    #write data cell contact

    cell_contact.add_paragraph(contact["first_name"] + " " +  contact["last_name"])
    cell_contact.add_paragraph("tel: " + contact["phone"])
    cell_contact.add_paragraph("Email: " + contact["email"])
    cell_contact.add_paragraph("Domicile: " + contact["residence"])
    cell_contact.add_paragraph(contact["mention"])

    #weite data cell title
    cell_title.add_paragraph(title["title"])



#trainings part
def training_part(document, training):

    #taining part title
    training_title= document.add_paragraph("Formations")

    #write trainings
    for i, trn in enumerate(training,1):
        document.add_paragraph(trn["title"] + " " + trn["school"] + " " + trn["date_start"] + ":" + trn["date_end"])
#professionnal experiences
def pro_experiences_part(document, experience):
    #experiences title
    exp_title= document.add_paragraph("Expériences professionnelles : ")

    #weite experiences
    for i, exp in enumerate(experience,1):
        document.add_paragraph(exp["title"] + " " + exp["company"] + " " + exp["date_start"] + ":" + exp["date_end"] + ":" + exp["summary"])


#technical skills
def tech_skills(document, skills):

    #technical skills title
    skills_title = document.add_paragraph("Compétences techniques")
    #write skills
    document.add_paragraph(skills)

#write professionnal skills
def pro_skills(document, skills):

    #professionnal skills title
    pro_title= document.add_paragraph("Compétences professionnelles")

    #write professionnal skills
    document.add_paragraph(skills)



#personal project
def perso_projects(document, projects):

    #personal project title
    document.add_paragraph("Projets personnels")

    #write personal projects
    for i, prj in enumerate(projects,1):


        project_label= document.add_paragraph(prj["title"]  + ": " +  prj["summary"])
        project_link = document.add_paragraph(prj["link"])

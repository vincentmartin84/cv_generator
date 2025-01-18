from docx import  Document

def create_file():
    cv_doc = Document()
    return cv_doc

def save_file(document, name_file):
    document.save(name_file )


def write_contact_details(document, data):
    names = document.add_paragraph(data["first_name"] + " " +  data["last_name"])
    phone = document.add_paragraph(data["phone"])
    email = document.add_paragraph(data["email"])
    mention = document.add_paragraph(data["mention"])

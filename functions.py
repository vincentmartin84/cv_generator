import curses.ascii
import re
from datetime import datetime
#valided names
def valided_names(name):
    if all(c.isalpha() or c == ' ' or c == '-' for c in name):
        return True
    else:
        return False


#valided email
def valided_email(email):
    regex_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(regex_email, email):
        return True
    else:
        return False

# Validate date function
def valided_date(date):
    try:
        datetime.strptime(date, "%d/%m/%Y")
        return True
    except ValueError:
        return False

# Compare the start and end dates
def compare_dates(start_date, end_date):
    start_date_obj = datetime.strptime(start_date, "%d/%m/%Y")
    end_date_obj = datetime.strptime(end_date, "%d/%m/%Y")
    return start_date_obj < end_date_obj

#valided file name
def valided_file_name(file):
    if all(c.isalpha() or c.isdigit() or c == "_" or c == "-" for c in file):
        return True
    else:
        return False


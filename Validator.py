#will check the expense and remove any white space, convert all to lower case if needed
from curses.ascii import isdigit


def check_transaction_type(transaction_type):
    t_type_str = str(transaction_type)
    t_type_str = t_type_str.strip()
    t_type_str = t_type_str.lower()
    t_type_str = t_type_str.replace(" ", "")
    
    if t_type_str == "expense" or t_type_str == "income":
        return t_type_str
    else:
        return "Error: incorrect transaction type"


def check_amount(amount):
    try:
        #cast operation fails when it encounters a thing it cant convert
        float(amount)
        return True
    except:
        print("Error: invalid data entered in amount field")#for debugging purposes, remove when not needed
        return False
    
# i dont need this because of the date and time module but I am gonna have to do a massive rewrite(or not really because oop baby)
def check_date(date):
    # date format is dd/mm/yyyy
    split_date = date.split("/")
    #checking if it is even the correct length
    if len(split_date) == 3:
        day = split_date[0]
        month = split_date[1]
        year = split_date[2]
        #check if they're numbers
        if day.isdigit() == True and month.isdigit() and year.isdigit():
            #checking if the date is within range
            None
        
        else:
            raise Exception("date numerical error: One of the fields are not a valid number, please check the date and try again") 
    else:
        raise Exception("dates only have 3 fields, day/month/year nothing more")
    
def check_username(username):
    code = None
    u = str(username)
    if len(u) <= 4:
        code = -1
    else:
        code = 1
        
    return code
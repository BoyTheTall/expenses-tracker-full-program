#will check the expense and remove any white space, convert all to lower case if needed
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
        
def check_date(date):
    NotImplemented
    
def check_username(username):
    code = None
    u = str(username)
    if len(u) <= 4:
        code = -1
    else:
        code = 1
        
    return code
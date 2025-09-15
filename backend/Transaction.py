from re import split
import sqlite3
import random
import string
import time
import datetime

class transaction:
    transaction_type = None #for denoting if it is an expense or income. I will have to use data validation to check if it is one of two values
    amount = None
    category = None
    transaction_id = None
    date = None
    
    def __init__(self, t_id, amount, category, transaction_type, date):
        #the date will use / as a separator and in the format dd/mm/yyyy
        split_date = date.split("/")
        year = int(split_date[2])
        month = int(split_date[1])
        day = int(split_date[0])
        self.transaction_type = transaction_type
        self.amount = amount
        self.category = category
        self.transaction_id = t_id
        self.date = datetime.date(year, month, day)
            
    def getTransactionType(self) -> str:
        return self.transaction_type
    
    def getTransactionId(self) -> int:
        return self.transaction_id
    
    def getAmount(self) -> float:
        return self.amount
    
    def getCategory(self) -> str:
        return self.category
    
    #this will return a string because that is what the rest of the architecture expects
    def getDate(self) -> str:
        return self.date.strftime("%d") + "/" + self.date.strftime("%m") + "/" + self.date.strftime("%Y")
        
    def setTransactionType(self, transaction_type) -> None:
        self.transaction_type = transaction_type
        
    def setTransactionID(self, transaction_id) -> None:
        self.transaction_id = transaction_id
        
    def setAmount(self, amount) -> None:
        self.amount = amount
    
    def setCategory(self, category) -> None:
        self.category = category
    
    def setDate(self, date) -> None:
        split_date = date.split("/")
        year = int(split_date[2])
        month = int(split_date[1])
        day = int(split_date[0])
        self.date = datetime.date(year, month, day)
        
    def toString(self) -> string:
        t_string  = f"""
        Transaction Details
        Transaction ID: {self.getTransactionId()}
        Amount: {self.getAmount()}
        Category: {self.getCategory()}
        Transaction Type: {self.getTransactionType()}
        Date: {self.getDate()}
        """
        return t_string
    
class transaction_services:
    db_conn = None #to be used for the data base connection
    db_directory = "backend/transactions.db"
    cursor = None
    #constants
    MONTH_AND_YEAR = "month and year"
    SPECIFIC_DATE = "specific date"
    
    
    def __init__(self):
        self.initialise_conn()
    
    def initialise_conn(self):
        self.db_conn = sqlite3.connect(self.db_directory)
        self.cursor = self.db_conn.cursor()
        
    
    def create_tables(self) -> None:
        sql_statement = """CREATE TABLE
        transactions(transaction_id, Amount, Category, Transaction_Type, Date)
                    
        """
        self.cursor.execute(sql_statement)
        
    def add_transaction(self, transaction_t) -> None:
        sql_statement = f"""INSERT INTO transactions VALUES ({transaction_t.getTransactionId()}, {transaction_t.getAmount()},
        '{transaction_t.getCategory()}', '{transaction_t.getTransactionType()}', '{transaction_t.getDate()}')"""
        self.cursor.execute(sql_statement)
        self.db_conn.commit()
        
            
    def getExpenses(self) -> list:
        sql_statement = f"SELECT * FROM transactions WHERE Transaction_Type = \"expense\""
        res = self.cursor.execute(sql_statement)
        result_set = list(res.fetchall())#list
        expenses = list([])
        for i in range(0, len(result_set)):
            #the lists within the resul set list are 5 items long/wide
            transaction_id = result_set[i][0]
            amount = result_set[i][1]
            category = result_set[i][2]
            transaction_type = result_set[i][3]
            date = result_set[i][4]
            t = transaction(transaction_id, amount, category, transaction_type, date)
            expenses.append(t)

        return expenses
    
    #I likely wont use this function because the getTransactions function can have the same functionality
    def getTransaction(self, transaction_id) -> list:
        sql_statement= f"SELECT * FROM transactions WHERE transaction_id = {transaction_id}"
        res = self.cursor.execute(sql_statement)
        result_set = res.fetchone()
        t_id = result_set[0]
        amount = result_set[1]
        category = result_set[2]
        transaction_type = result_set[3]
        date = result_set[4]
        transaction_t = transaction(t_id, amount, category, transaction_type, date)
        return transaction_t
    
    #needs to be tested date type will be used to distinguish what type of date we have, a specific or a general one with a month and year only. I should make a function that gets a years transactions later
    def getTransactions(self, t_id=None, date=None, category=None, t_type= None, date_type=None) -> str:
        
        sql = "SELECT * FROM transactions"
        parameter_added = False
        if t_id != None:
            if parameter_added == False:
                sql += f" WHERE transaction_id = {t_id}"
                parameter_added = True
            else:
                sql += f" AND transaction_id = {t_id}"
                
        if date != None:
            if parameter_added == False:
                if date_type == "specific date":
                    sql += f" WHERE Date = '{date}'"
                
                else:
                    sql += f" WHERE DATE LIKE '%{date}'"
                    
                parameter_added = True
            else:
                if date_type == "specific date":
                    sql += f" AND Date = '{date}'"
                
                else:
                    sql += f" AND DATE LIKE '%{date}'"
        
        if category != None:
            if parameter_added == False:
                sql += f" WHERE Category = '{category}'"
                parameter_added = True
            else:
                sql += f" AND Category = '{category}'"
        
        if t_type != None:
            if parameter_added == False:
                sql += f" WHERE Transaction_Type = '{t_type}'"
                parameter_added = True
            else:
                sql += f" AND Transaction_Type = '{t_type}'"
        
        result_set = self.cursor.execute(sql)
        result_set = list(result_set.fetchall())
        transactions = tranverse_result_set(result_set=result_set)
        return transactions
        
            
    #this will assume that the things to update is already in the state of the transaction object, the transaction id will never change
    def update_transaction(self, transaction_t) -> None:
        sql_statement = f"""UPDATE transactions
                SET amount = {transaction_t.getAmount()}, Category = '{transaction_t.getCategory()}', Transaction_Type = '{transaction_t.getTransactionType()}', Date = '{transaction_t.getDate()}'
                WHERE transaction_id = {transaction_t.getTransactionId()}"""
        self.cursor.execute(sql_statement)
        self.db_conn.commit()
    
    #this wont be called by external code because the delete_multiple transactions can provide the same functionality of deleting one function
    def delete_transaction(self, t_id) -> None:
        sql = f"""DELETE FROM tblTransactions WHERE transaction_id = {t_id}"""
        self.cursor.execute(sql)
        self.db_conn.commit()
    
    def delete_multiple_transactions(self, transaction_list) -> None:
        for i in range(0, len(transaction_list)):
            self.delete_transaction(transaction_list[i].getTransactionID())

def generate_ID() -> int:
    db_id = int(time.time() + random.randint(0, int(time.time())))
    return db_id

#this will be used to traverse result sets that will have multiple results but I should have code where it will bring up one record properly
def tranverse_result_set(result_set) -> list:
    transactions = list([])
    for i in range(0, len(result_set)):
        #the lists within the resul set list are 5 items long/wide
        transaction_id = result_set[i][0]
        amount = result_set[i][1]
        category = result_set[i][2]
        transaction_type = result_set[i][3]
        date = result_set[i][4]
        t = transaction(transaction_id, amount, category, transaction_type, date)
        transactions.append(t)
            
    return transactions
    
#We should probably add a data validation thing at some point because users decide to do a funny and put in bad input
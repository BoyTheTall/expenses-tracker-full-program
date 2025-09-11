import sqlite3

class Transaction_Insights:
    db_conn = None
    db_directory = "transactions.db"
    cursor = None
    
    def __init__(self):
        self.db_conn = sqlite3.connect(self.db_directory)
        self.cursor = self.db_conn.cursor()
    
    def getMonthlyExpenses(self, month, year): #will always group by category
        sql = f"SELECT Category, SUM amount AS Total FROM tblExpenses WHERE Month =""%{month}/{year}"""
    
    def getYearlyExpenses(self, year, grouping_column = None): #if grouping column is none existent then default grouping will be by month
        pass
    
    def getExpensesByCategory(self, category):
        pass
    
    def getMonthlyIncome(self, month):
        pass
    
    def getYearlyIncome(self, year):
        pass
import sqlite3

class Portfolio:
    #can be used for overall portfolio details or the portfolio snapshots. just name it properly when using it
    snapshot_id = None
    current_value = None
    money_deposited = None
    date =  None #current date or latest date of information
    gain = None
    
    def __init__(self, current_value, money_deposited, date) -> None:#use when its not a snapshot
        self.current_value = current_value
        self.money_deposited = money_deposited
        self.date = date
        self.gain = current_value - money_deposited
    
    def __init__(self, snapshot_value, money_deposited, snapshot_date, snapshot_id):#use when it is a snapshot
        self.snapshot_id = snapshot_id
        self.current_value = snapshot_value
        self.money_deposited = money_deposited
        self.date = snapshot_date
        self.gain = self.current_value - self.money_deposited
        
        
    def getCurrentValue(self):
        return self.current_value
    
    def getMoneyDeposited(self):
        return self.money_deposited
    
    def getDate(self):
        return self.date
    
    def getGain(self):
        return self.gain
    
    def setCurrentValue(self, P_value):
        self.current_value = P_value
        self.updateGain()
    
    def setMoneyDeposited(self, d_money):
        self.money_deposited = d_money
        self.updateGain()
    
    def setDate(self, c_date):
        self.date = c_date
    
    def updateGain(self):
        self.gain = self.current_value - self.money_deposited
        
class Portfilio_Services:
    db_conn = None
    db_directory = "portfolio.db"
    cursor = None
    
    def __init__(self):
        self.db_conn = sqlite3.connect(self.db_directory)
        self.cursor = self.db_conn.cursor()
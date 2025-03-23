class portfolio:
    current_value = None
    money_deposited = None
    date =  None
    gain = None
    
    def __init__(self, current_value, money_deposited, date) -> None:
        self.current_value = current_value
        self.money_deposited = money_deposited
        self.date = date
        self.gain = current_value - money_deposited
        
    def getCurrentValue(self):
        return self.current_value
    
    def getMoneyDeposited(self):
        return self.money_deposited
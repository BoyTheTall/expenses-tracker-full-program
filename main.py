import backend.Transaction as Transaction

date = "12/10/2023"
t_id = 1
amount = 900.45
transaction_type = "expense"
category = "groceries"

t = Transaction.transaction(t_id, amount, category, transaction_type, date)
print(t.toString())
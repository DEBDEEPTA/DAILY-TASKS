"""
A DataFrame contains account_id, transaction_date, amount, and transaction_type.
"""
from faker import Faker
import datetime
import pandas as pd
def generate_transaction_df():
    fk = Faker()
    transaction_type_list = ["UPI", "CARD", "ATM"] # CONSIDERING 3 TRANSACTION TYPES
    account_id_list = list( fk.iban() for _ in range(101)) # 100 UNIQUE ACCOUNT ID'S

    date_start = datetime.date(2021,1,1)
    date_end = datetime.date(2025,12,31)


    account_id = []
    transaction_date = []
    amount = []
    transaction_type = []

    data = {
    "account_id": account_id,
    "transaction_date": transaction_date,
    "amount": amount,
    "transaction_type": transaction_type
    }

    # CONSIDERING 300 RECORDS
    for _ in range(300):
        account_id.append(fk.random_element(account_id_list))
        transaction_date.append(fk.date_between_dates(date_start,date_end))
        # considering max ammount/transaction (credit) -> 1l
        # considering min ammount/transaction (debit)  -> -1l
        amount.append(fk.random_int(-100000, 100000))
        transaction_type.append(fk.random_element(transaction_type_list))

    df = pd.DataFrame(data)
    return df

if __name__=="__main__":
    print(generate_transaction_df().head(100))
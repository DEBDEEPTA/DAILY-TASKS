"""
Pandas (Intermediate)
A DataFrame contains account_id, transaction_date, amount, and transaction_type.
Task:
    Aggregate daily transaction totals per account
    Identify accounts with unusually high transaction volume
    Detect potential fraud using statistical thresholds
"""
from helper.generator import generate_transaction_df

def net_daily_trns_per_acc(data):
    data_grp_by_date = data.groupby(["account_id","transaction_date"])["amount"].sum()

    return data_grp_by_date

def  acc_with_high_transaction_val(data,threshold = 50000):
    """ Considering a transaction as high value transaction if it's more than 50,000"""

    filter_mask = data["amount"] > threshold

    filtered_data = data[filter_mask]
    return filtered_data["account_id"].unique()

if __name__=="__main__":

    data = generate_transaction_df()
    print(f"Sample Data\n{data.head(10)}")

    print(f"daily transaction totals per account\n{net_daily_trns_per_acc(data)}")

    print(f"Account with high transaction vals:\n{acc_with_high_transaction_val(data)}")
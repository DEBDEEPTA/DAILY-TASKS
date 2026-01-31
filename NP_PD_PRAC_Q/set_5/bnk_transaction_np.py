"""
NumPy (Intermediate)
A bank stores transaction amounts for 50 accounts across 20 days in a NumPy array.
Task:
    Separate debit and credit transactions
    Compute daily net balance changes
    Identify accounts with continuous negative balance trends
"""
import numpy as np



def debited_credited_trans(data):
    credited_data = data[data>0]
    debited_data = data[data<0]

    print(f"Debit Transactions\n{debited_data}")
    print(f"Credited Transactions\n{credited_data}")

def daily_net_balance_changes(data):
    net_balance = data.sum(axis=1)
    return net_balance

def continous_nve_bal_trend_aprch_1(data):

    """
        APPROACH_1
         -> considering a account falls under negative bal. trend if for all 20 days it have negative balance
    """
    # boolean mask for negative values
    neg_mask = (data<0)

    # return boolean mask for all negative values
    neg_trend_acc = np.all(neg_mask, axis=0)

    neg_trend_acc_index = np.where(neg_trend_acc)[0]
    print(neg_trend_acc_index)

def continous_nve_bal_trend_aprch_2(data, threshoald_day = 5):
    """
        APPROACH_2
            -> consider a account falls under negative bal trend if negative bal. are consecutive for n days
            -> threshoald_day -> min consecutive days for which a account will consider as negative trend acc. (Default -> 5)

        LOGIC ->
              -> obtain boolean mask for negative values
              -> count consecutive True values for each account for everyday
              -> maintain counter for consecutive true values
              -> if counter >= threshoald print the index for the account (outer loop index)
    """

    neg_mask = (data<0)
    days,accounts = neg_mask.shape
    neg_trends_accounts = []

    for acc in range(accounts):
        count = 0
        max_count = 0
        for day in range(days):
            if neg_mask[day,acc]:
                count += 1
                max_count = max(max_count,count)
            else:
                count = 0

        if max_count >= threshoald_day:
            neg_trends_accounts.append(acc)

    return neg_trends_accounts

if __name__=="__main__":

    # CONSIDERING MAXIMUM SALARY CAN BE DEBITED/TRANSACTION   -> -1L
    # CONSIDERING MINIMUM SALARY CAN BE CREDITED/TRANSACTION -> 1L
    data_trans = np.random.randint(-100000,100000,(20,50))

    print(f"Sample Data :\n{data_trans}")

    debited_credited_trans(data_trans)
    print(f"Daily Net Balance Changes\n{daily_net_balance_changes(data_trans)}")

    print(f"Accounts with continuous negative_bal. Trends\n{continous_nve_bal_trend_aprch_2(data_trans)}")
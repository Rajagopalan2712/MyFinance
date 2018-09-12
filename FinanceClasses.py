from datetime import date


class Transaction:
    def __init__(self, txn_date: date, merchant, category, amount, account, txn_type):
        self.txn_date = txn_date
        self.merchant = merchant
        self.category = category
        self.amount = amount
        self.account = account
        self.txn_type = txn_type

    def __str__(self):
        return self.txn_date.__str__()+","+self.merchant+","+self.category+","+self.amount+","+self.account+","+self.txn_type+","+"\n"
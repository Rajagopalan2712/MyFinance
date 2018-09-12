
import FinanceClasses
import FinanceUtil
import csv
from pathlib import Path

class Transactions:
    def __init__(self):
        self.credit_transactions = []
        self.credit_card_purchases = []
        with open(Path.home()._make_child_relpath("/Documents/FinanceData/creditTxn.csv")) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                transaction = FinanceClasses.Transaction(FinanceUtil.datetime_from_string(row[0]), row[1], row[2],
                                                         row[3], row[4], row[5])
                self.credit_transactions.append(transaction)
        with open(Path.home()._make_child_relpath("/Documents/FinanceData/debitTxn.csv")) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                transaction = FinanceClasses.Transaction(FinanceUtil.datetime_from_string(row[0]), row[1], row[2],
                                                         row[3], row[4], row[5])
                self.credit_card_purchases.append(transaction)

    def __init__(self, file_path: str):
        self.credit_transactions = []
        self.credit_card_purchases = []
        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_num = 0
            for row in csv_reader:
                if line_num == 0:
                    line_num = 1
                    continue
                transaction = FinanceClasses.Transaction(FinanceUtil.datetime_from_string(row[0]), row[1], row[5],
                                                         row[3], row[6], row[4])
                if "credit" == row[4]:
                    self.credit_transactions.append(transaction)
                elif "debit" == row[4] and row[6] != "TOTAL CHECKING":
                    self.credit_card_purchases.append(transaction)
            self.credit_transactions.sort(key=lambda t: t.txn_date, reverse=True)
            self.credit_card_purchases.sort(key=lambda t: t.txn_date, reverse=True)
            credit_txn_file = open(Path.home()._make_child_relpath("/Documents/FinanceData/creditTxn.csv"), "w")
            for txn in self.credit_transactions:
                credit_txn_file.write(txn.__str__())
            debit_txn_file = open(Path.home()._make_child_relpath("/Documents/FinanceData/debitTxn.csv"), "w")
            for txn in self.credit_card_purchases:
                debit_txn_file.write(txn.__str__())
            print("Completed loading  " + str(self.credit_transactions.__sizeof__()) + " new credit records and " + str(
                self.credit_card_purchases.__sizeof__()) + " new debit records and ready to compute")

    def generate_report_by_merchant(self, month: int, year: int):
        txn_map = {}
        for txn in self.credit_card_purchases:
            if txn.txn_date.month == month and txn.txn_date.year == year:
                if txn.merchant in txn_map:
                    txn_amount = txn_map[txn.merchant]
                    txn_map[txn.merchant] = float(txn.amount) + txn_amount
                else:
                    txn_map[txn.merchant] = float(txn.amount)

        return txn_map

    def is_category_defined(self):
        categoryRules = Path("/path/to/file")

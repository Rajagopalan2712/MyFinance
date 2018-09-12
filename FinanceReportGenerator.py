from TxnDataStructure import Transactions
from pathlib import Path
import os

transactions = None
fin_data_dir = os.path.expanduser("~")+"/Documents/FinanceData/"
fin_data_file_path = fin_data_dir+"transactions.csv"

txnFile = Path(fin_data_file_path)
if not txnFile.is_file():
    print(
        "transactions.csv file is not found at " + fin_data_dir
        + ". Please ensure the file is present")
else:
    transactions = Transactions(fin_data_file_path)

if not transactions:
    quit(1)

print("To generate report, please enter month and year")
month = int(input("Enter Month : "))
year = int(input("Enter Year : "))

txn_map = transactions.generate_report_by_merchant(month, year)
for entry in txn_map:
    print(entry + " : " + str(txn_map[entry]))

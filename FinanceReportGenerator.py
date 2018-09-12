from TxnDataStructure import Transactions

transactions = None

print("Please choose from below options")
print("To use existing transaction records, enter 1")
print("To provide new transaction records, enter 2")
userInput = int(input("Enter your input :"))


if userInput == 2:
    input_file = input("Provide the path for new transactions file : ")
    transactions = Transactions(input_file)

elif userInput == 1:
    transactions = Transactions()

print("To generate report, please enter month and year")
month = int(input("Enter Month : "))
year = int(input("Enter Year : "))

txn_map = transactions.generate_report_by_merchant(month, year)
for entry in txn_map:
    print(entry+" : "+str(txn_map[entry]))
from Except import InsufficientFundError, amount
import pickle

def withdraw():
    records = []

    try:
        accno = int(input("Enter your account number: "))
        amou = int(input("Enter how much amount you want to withdraw: "))
        if amou <= 0:
            print("Invalid amount.")
            return
    except ValueError:
        print("Don't enter alphabets, strings or special symbols.")
        return

    try:
        with open("bankdetails.data", "rb") as fp:
            while True:
                try:
                    record = pickle.load(fp)
                    records.append(record)
                except EOFError:
                    break
    except FileNotFoundError:
        print("File doesn't exist.")
        return

    recno = -1
    for i, record in enumerate(records):
        if record[0] == accno:
            recno = i
            break

    if recno == -1:
        print("Your account does not exist.")
        return

    try:
        records[recno][3] = amount(records[recno][3] - amou)
    except InsufficientFundError:
        print("You don't have enough amount to withdraw.")
        return

    try:
        with open("bankdetails.data", "wb") as wp:
            for rec in records:
                pickle.dump(rec, wp)
        print(f"Withdrawal of ₹{amou} is successful.")
    except Exception as e:
        print("Error writing to file:", e)


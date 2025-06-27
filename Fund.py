import pickle
from Except import InsufficientFundError, amount

def transfunds():
    records = []
    try:
        with open("bankdetails.data", "rb") as fp:
            while True:
                try:
                    record = pickle.load(fp)
                    records.append(record)
                except EOFError:
                    break
    except FileNotFoundError:
        print("File not exist")
        return

    try:
        accno1 = int(input("Enter your account number: "))
    except ValueError:
        print("Don't enter alphabets, strings, or special symbols.")
        return

    rno1 = -1
    for i, record in enumerate(records):
        if record[0] == accno1:
            rno1 = i
            break

    if rno1 == -1:
        print(f"Account number {accno1} does not exist.")
        return

    try:
        accno2 = int(input("Enter recipient's account number: "))
    except ValueError:
        print("Don't enter alphabets, strings, or special symbols.")
        return

    rno2 = -1
    for i, record in enumerate(records):
        if record[0] == accno2:
            rno2 = i
            break

    if rno2 == -1:
        print(f"Account number {accno2} does not exist.")
        return

    try:
        amo = int(input("Enter how much amount you want to transfer: "))
        if amo <= 0:
            print("Invalid amount.")
            return
    except ValueError:
        print("Don't enter alphabets, strings, or special symbols.")
        return

    try:
        amou = amount(records[rno1][3] - amo)
    except InsufficientFundError:
        print("You have no sufficient amount to transfer.")
        return

    records[rno1][3] -= amo
    records[rno2][3] += amo

    try:
        with open("bankdetails.data", "wb") as wp:
            for rec in records:
                pickle.dump(rec,wp)
        print(f"Amount {amo} is successfully transferred.")
    except Exception as e:
        print("Error writing to file:", e)

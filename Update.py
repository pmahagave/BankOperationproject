import pickle

def deposit():
    records = []

    try:
        accno = int(input("Enter Account Number: "))
    except ValueError:
        print("Invalid input. Only numbers allowed.")
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

    rno = -1
    for i, record in enumerate(records):
        if record[0] == accno:
            rno = i
            break

    if rno == -1:
        print("Account number does not exist.")
        return

    try:
        amount = int(input("Enter how much money you want to deposit: "))
        if amount <= 0:
            print("Invalid amount.")
            return
    except ValueError:
        print("Invalid input. Only numbers allowed.")
        return

    records[rno][3] += amount

    try:
        with open("bankdetails.data", "wb") as wp:
            for rec in records:
                pickle.dump(rec, wp)
        print(f"Amount {amount} successfully deposited to account {accno}.")
    except Exception as e:
        print("Error writing to file:", e)

# deposit()

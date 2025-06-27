import pickle

def searchAcc():
    try:
        accno = int(input("Enter your account number: "))
    except ValueError:
        print(" Invalid input. Please enter numbers only.")
        return

    found = False

    try:
        with open("bankdetails.data", "rb") as fp:
            while True:
                try:
                    record = pickle.load(fp)
                    if record[0] == accno:
                        print(f" Account Found:\nAccount No: {record[0]}\nName: {record[1]}\nBalance: ₹{record[3]}")
                        found = True
                        break
                except EOFError:
                    break
    except FileNotFoundError:
        print(" File does not exist.")
        return

    if not found:
        print(f" Account {accno} does not exist.")

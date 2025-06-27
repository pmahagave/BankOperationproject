from random import randint
import pickle
from Except import ZeroNamelengthError, SpaceError, InvalidError, validation

def openAccount():
    while True:
        with open("bankdetails.data", "ab") as fp:
            lst = []
            accno = randint(1000000000, 9999999999)

            try:
                custname = validation(input("Enter your name: "))
                pin = int(input("Enter 6-digit PIN for your account: "))
                if len(str(pin)) != 6:
                    print("Your PIN should contain exactly 6 digits. Try again.")
                    continue

                balance = int(input("Enter opening balance: "))
                if balance < 0:
                    print("Balance cannot be negative.")
                    continue

                lst.extend([accno, custname, pin, balance])
                pickle.dump(lst, fp)

                print("Your account has been successfully created.")
                print(f"{custname}, your account number is {accno}")
                break

            except ValueError:
                print("Invalid input! Only numbers are allowed for PIN and balance.")
            except ZeroNamelengthError:
                print("You must enter a name. Try again.")
            except SpaceError:
                print("Don't enter only spaces for your name. Try again.")
            except InvalidError:
                print("Invalid name. Try again.")

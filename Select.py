
import pickle
def alldetails():
    data=[]
    try:
        with open("bankdetails.data","rb")as rp:
            print("ACCOUNTNO\t\tNAME\t\tPIN\t\tBALANCE")
            while True:
                try:
                    record=pickle.load(rp)
                    data.append(record)
                except EOFError:
                    print("-"*50)
                    break
                for value in data:
                 for rec in value:
                    print("{}".format(rec),end="\t\t")
                 print()
    except FileNotFoundError:
        print("FILE DONT EXIST")

import pickle

def singleaccdetail():
    sa = []
    try:
        with open("bankdetails.data", "rb") as rp:
            try:
                accno = int(input("Enter your account number: "))
            except ValueError:
                print("Don't enter alphabets, strings, or special symbols.")
                return

            while True:
                try:
                    record = pickle.load(rp)
                    sa.append(record)
                except EOFError:
                    break

            res = False
            for i in range(len(sa)):
                if sa[i][0] == accno:
                    recno = i
                    res = True
                    break

            if res:
                print(" Account Found:")
                print("Account Number =", sa[recno][0])
                print("Name =", sa[recno][1])
                print("PIN =", sa[recno][2])
                print("Balance  = ₹", sa[recno][3])
            else:
                print(f"Account number {accno} does not exist.")
    except FileNotFoundError:
        print(" File does not exist.")

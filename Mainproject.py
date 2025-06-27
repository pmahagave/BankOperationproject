
from Menu import menu
from openAccount import openAccount
from Update import deposit
from Withdraw import withdraw
from Search import searchAcc
from Select import alldetails,singleaccdetail
from Fund import transfunds

while True:
      menu()
      try:
          ch=int(input("\t\tEnter Your Choice"))
          if len(str(ch))==1:
              match ch:
                  case 1:
                      openAccount()
                  case 2:
                      deposit()
                  case 3:
                      withdraw()
                  case 4:
                      searchAcc()
                  case 5:
                      alldetails()
                  case 6:
                      singleaccdetail()
                  case 7:
                      transfunds()
                  case 8:
                      print("THANKS FOR USING THIS PROGRAM")
                      break
          else:
              print("Invalid choice----try again")

      except ValueError:
          print("DON'T ENTER ALNUMS,STR AND SPECIAL SYMBOLS")




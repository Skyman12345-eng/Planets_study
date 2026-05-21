import time
import sys

trappist = (" 1. NAME: TRAPPIST-1E" , " 2. DISTANCE: 40LIGHT YEARS" , " 3. LIVE IS POSSIBLE")
kepler = ("1. NAME: KEPLER-452B" ,  "2. DISTANCE: 1452LIGHT YEARS" , "3. LIVE IS POSSIBLE")
Mars = ("1. NAME: MARS" , "2. DISTANCE: 0.5 A.E." , "3. LIFE IS NOT POSSIBLE")

print("Hello! Do you want to study planets?")
choose = input("Yes/No : ")
if choose.lower().strip() == "yes":
    print("1. TRAPPIST-1E" ,"2. KEPLER-452B" , "3. MARS")
    choice = input("WHICH PLANET WILL YOU CHOOSE? : ")
    if choice.lower().strip() == "1":
        for a in trappist:
            print(a)
    elif choice.lower().strip() == "2":
        for p in kepler:
            print(p)
    elif choice.lower().strip() == "3":
        for w in Mars:
            print(w)
    else:
        print("ERROR NUMBER")
else:
    print("BYE BYE 👋")
    sys.exit()                               
            
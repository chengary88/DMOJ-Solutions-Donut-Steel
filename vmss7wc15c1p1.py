hey = input()
phone1 = int(hey[0]) + int(hey[1]) + int(hey[2])
phone2 = int(hey[4]) + int(hey[5]) + int(hey[6])
phone3 = int(hey[8]) + int(hey[9]) + int(hey[10]) + int(hey[11])
if phone1 == phone2 and phone2 == phone3:
    print("Goony!")
else:
    print("Pick up the phone!")

import random
picks = []

userinput = int(input("How many picks?"))

for i in range(userinput):
    temp_picks = []
    for j in range(6):
        rand_no = random.randint(1, 45)
        while rand_no in temp_picks:
            rand_no = random.randint(1, 45)
        temp_picks.append(rand_no)
    picks.append(temp_picks.sort())
    print(temp_picks)

"""
CP1404/CP5632 = Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))



def getScore(score):
    if score < 0 :
        return("Invalid score")
    elif score > 100:
        return("Invalid score")
    elif score >= 90:
        return ("Excellent")
    else:
        return ("Bad")

print(getScore(score))
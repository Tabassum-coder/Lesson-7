Eng=int(input("Enter marks for English"))
Sci=int(input("Enter marks for Science"))
Maths=int(input("Enter marks for Maths"))
History=int(input("Enter marks for History"))
Hindi=int(input("Enter marks for Hindi"))

avg=(Eng+Sci+Maths+History+Hindi)/5

if avg>=90 and avg<=100:
    print("Grade is A1")
elif avg>=81 and avg<=90:
    print("Grade is A2")
elif avg>=71 and avg<=80:
    print("Grade is B1")
elif avg>=61 and avg<=70:
    print("Grade is B2")
elif avg>=51 and avg<=60:
    print("Grade is C1")
elif avg>=41 and avg<=50:
    print("Grade is C2")
elif avg>=31 and avg<=40:
    print("Grade is D1")
elif avg>=21 and avg<=30:
    print("Grade is D2")
elif avg>=11 and avg<=20:
    print("Grade is E1")
else:
    print("Grade is E2")
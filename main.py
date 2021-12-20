#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
Total = float(input("What was the total bill? $"))
Tip_per = float(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))
new_total = float(Total * ((100 + Tip_per)/100))
ppp = (round(new_total / people, 2))
n_ppp = "{:.2f}".format(ppp)
print(f"Each person should pay: ${n_ppp}")
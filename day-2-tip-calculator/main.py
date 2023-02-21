total_bill = float(input('Welcome to the tip calculator\nWhat was the total bill? '))

pct_tip = int(input('What percentage tip would you like to give? '))/100

no_of_people = int(input('How many people to split the bill? '))

total_bill_tip = total_bill + (total_bill*pct_tip)

amount_per_person = round(total_bill_tip/no_of_people, 2)

print(f'Each person should pay {amount_per_person}')
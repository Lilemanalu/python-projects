print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $")
tip_percentage = input("How much tip would you like to give? 10, 12, or 15? ")
number_of_people = input("How many people to split the bill? ")

bill_per_person = (float(total_bill) / float(number_of_people)) * (float(tip_percentage) /100)

print(f"Each person should pay: ${round((float(total_bill) / float(number_of_people)) + bill_per_person,2)}")
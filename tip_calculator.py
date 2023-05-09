print("Welcome to the tip calculator")
total_bill = input("What was the total bill? ")
tip_percent = input("What percentage tip would you like to give? ")
num_of_people = input("How many people are splitting the bill? ")

# if int(tip_percent) < 12:
#   print("Lol stingy")

bill_per_person = (float(total_bill) + (float(total_bill) * (int(tip_percent)/100)))/int(num_of_people)

print(f"Each person should pay {bill_per_person}")
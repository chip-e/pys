age_years = input("What's your current age? ")
age_months = input("Months since last birthday? ")

weeks_lived = int(age_years) * 52 + int(age_months) * 4
weeks_left = (90 * 52) - weeks_lived
print(f"You have around {weeks_left} weeks left if you were to live til 90")

# graphic = ""
# for x in range(int(weeks_lived)):
#     if x % 52 == 0:
#         graphic += "\n"
#     graphic += "*"

# print(graphic)

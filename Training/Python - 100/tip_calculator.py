print("Welcome to the tip calculator")
bill_cost = float(input("How much was the bill? : "))
tip_percent = int(input("what percentage are you wanting to tip? 10, 12, or 15? :"))
people_split = int(input("How many people are splitting the bill? : "))
#alternate  - tot_bill = bill_cost * (1 + tip_percent / 100)
tot_bill = tip_percent / 100 * bill_cost + bill_cost
tot_per_person = tot_bill / people_split
abs_tot_bill = round(tot_per_person, 2)

print(f"The total cost per person is ${abs_tot_bill}")
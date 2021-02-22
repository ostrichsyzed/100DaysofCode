print("Welcome to my tip calculator!\nWe believe in treating our service industry fairly.\nLet's calculate that tip!")
total_bill = input("What was the total bill? $")
tip_percent = input("What percentage tip would you like to give? 12, 15, or 20? ")
num_ppl = input("How many people are splitting the bill? ")

tip = float(total_bill) * (float(tip_percent) / 100)
total = float(total_bill) + float(tip)
each_person = float(total) / float(num_ppl)

split_tip = round(float(each_person), 2)
print(f"Each person should pay: ${split_tip}")

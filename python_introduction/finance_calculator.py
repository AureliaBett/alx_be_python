income = int (input("Enter your monthly income: "))
expenses = int (input("Enter your monthly expenses: "))
savings = income - expenses
interest_rate = 0.05
projected_savings = savings * 12 + (savings * 12 * interest_rate)
print("Your monthly savings are:", savings)
print("Projected savings for the next year with interest is:", projected_savings)
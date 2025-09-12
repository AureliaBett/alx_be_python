monthly_income = int (input("Enter your monthly income: "))
monthly_expenses = int (input("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
interest_rate = 0.05
projected_savings = savings * 12 + (monthly_savings * 12 * interest_rate)
print("Your monthly savings are:", monthly_savings)
print("Projected savings for the next year with interest is:", projected_savings)
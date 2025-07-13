income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = income - expenses

annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

print(f"\nYour monthly savings are: ${monthly_savings:.2f}")
print(f"Your projected savings after one year (with 5% interest) are: ${projected_savings:.2f}")

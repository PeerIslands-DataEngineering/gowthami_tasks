import pandas as pd

data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hannah'],
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance', 'IT', 'HR'],
    'Age': [25, 32, 29, 41, 37, 45, 26, 38],
    'Salary': [50000, 70000, 65000, 80000, 75000, 90000, 62000, 85000],
    'Experience': [2, 7, 5, 15, 10, 20, 3, 12]
}

df = pd.DataFrame(data)

# Task 1: Average salary by department
avg_salary = df.groupby('Department')['Salary'].mean()
print("Average Salary by Department:\n", avg_salary, "\n")

# Task 2: Highest-paid employee in each department
highest_paid = df.loc[df.groupby('Department')['Salary'].idxmax()][['Department', 'Employee', 'Salary']]
print("Highest Paid Employee in Each Department:\n", highest_paid, "\n")

#  Task 3: Count employees with >5 years experience and salary > 65,000
filtered = df[(df['Experience'] > 5) & (df['Salary'] > 65000)]
count_filtered = filtered.shape[0]
print("Employees with >5 Years Experience and Salary > $65,000:", count_filtered, "\n")

# Task 4: Add 'Seniority' column
def classify_seniority(exp):
    if exp < 5:
        return "Junior"
    elif 5 <= exp <= 10:
        return "Mid-Level"
    else:
        return "Senior"

df['Seniority'] = df['Experience'].apply(classify_seniority)
print("DataFrame with Seniority:\n", df[['Employee', 'Experience', 'Seniority']], "\n")

# Task 5: Sort IT department employees by salary (descending)
it_sorted = df[df['Department'] == 'IT'].sort_values(by='Salary', ascending=False)
print("Sorted IT Department Employees by Salary:\n", it_sorted[['Employee', 'Department', 'Salary']])





import numpy as np

# Task 1: Create (30, 5) array of stock prices between $100 and $500
np.random.seed(42)  # for reproducibility
stock_prices = np.random.randint(100, 501, size=(30, 5))
print("Stock Prices (First 5 Days):\n", stock_prices[:5], "\n")

# Task 2: Average stock price for each company
avg_prices = stock_prices.mean(axis=0)
print("Average Stock Prices (per company):", avg_prices, "\n")

# Task 3: Highest stock price and its day and company
max_price = stock_prices.max()
max_index = np.unravel_index(np.argmax(stock_prices), stock_prices.shape)
max_day, max_company = max_index
print(f"Highest price recorded: ${max_price} at Day {max_day}, Company {max_company}\n")

# Task 4: Normalize prices to [0, 1] using min-max normalization
min_val = stock_prices.min()
max_val = stock_prices.max()
normalized_prices = (stock_prices - min_val) / (max_val - min_val)
print("Normalized Prices (First 5 Days):\n", np.round(normalized_prices[:5], 2), "\n")

# Task 5: Flag days with any stock < $200
risky_days = np.any(stock_prices < 200, axis=1)
print("Risky Investment Days:")
for i, is_risky in enumerate(risky_days):
    if is_risky:
        risky_stocks = stock_prices[i][stock_prices[i] < 200]
        print(f"Day {i + 1}: {risky_stocks.tolist()}")

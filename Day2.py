# Problem 1: Robust Calculator
# 🔹 Problem Statement:
# You are building a calculator that takes two numbers and an operator (+, -, *, /, %, **).
# •Handle invalid operations.
# •Handle division by zero.
# •Handle incorrect input types.
# Stubbed Code:
def calculator(a, b, operator):
    """
    Performs a calculation based on the given operator.
    
    :param a: First number (int/float)
    :param b: Second number (int/float)
    :param operator: String representing an operation (+, -, *, /, %, **)
    :return: Computed result or error message
    """
    try:
        # Perform operation
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            if b == 0:
                raise ZeroDivisionError("Division by zero")
            return a / b
        elif operator == "%":
            if b == 0:
                raise ZeroDivisionError("Modulo by zero")
            return a % b
        elif operator == "**":
            return a ** b
        else:
            raise ValueError("Unsupported operator")

    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Invalid input type"
    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"Unexpected error: {e}"

# Example Usage:
print(calculator(10, 0, "/"))       # Output: "Error: Division by zero"
print(calculator(10, "five", "+"))  # Output: "Error: Invalid input type"
print(calculator(10, 5, "$"))       # Output: "Error: Unsupported operator"
print(calculator(2, 3, "**"))       # Output: 8






# Problem 2: Nested Exception Handling – Banking System
# 🔹 Problem Statement:
# Simulate a banking system where users can withdraw money from their account.
# •Raise ValueError if the amount is negative.
# •Raise InsufficientFundsError if the withdrawal amount is greater than the balance.
# •Handle unexpected exceptions gracefully.
# Stubbed Code:
class InsufficientFundsError(Exception):
    """Custom exception for insufficient balance"""
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        """
        Withdraws money from the account.
        
        :param amount: Amount to withdraw
        :return: Remaining balance or error message
        """
        try:


            if amount < 0:
                raise ValueError("Withdrawal amount cannot be negative")

            if amount > self.balance:
                raise InsufficientFundsError("Insufficient balance")

            self.balance -= amount
            return f"Withdrawal successful. Remaining balance: ₹{self.balance:.2f}"

        except ValueError as ve:
            return f"Error: {ve}"
        except InsufficientFundsError as ie:
            return f"Error: {ie}"
        except Exception as e:
            return f"Unexpected error: {e}"

# Example Usage:
account = BankAccount(100)
print(account.withdraw(150))   # Output: Error: Insufficient balance
print(account.withdraw(-10))   # Output: Error: Withdrawal amount cannot be negative
print(account.withdraw(50))    # Output: Withdrawal successful. Remaining balance: ₹50.00

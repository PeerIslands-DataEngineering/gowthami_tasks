# def is_prime(x):
#     for i in range(2,int(x**0.5)+1 ):
#         if x%i==0:
#             return False
#     return True


# n=int(input("Enter size of list:"))
# li=[]
# for i in range(0,n):
#     x=int(input("Enter a value"))
#     while not is_prime(x):
#         x=int(input("Not a prime number,Enter a value: "))
#         li.append(x)

# print(li)


#Program 1

# def count_freq(paragraph):
#     dic={}
#     for row in paragraph:
#         for word in row:
#             lower_word= word.lower()
#             if lower_word =="stop":
#                 break
#             if len(lower_word)<3:
#                 continue
#             if lower_word in dic:
#                 dic[lower_word]+=1
#             else:
#                 dic[lower_word]=1
#         else:
#             continue
#         break
#     return dic

    
                
            
# paragraph = [
#     ["Hello", "world", "hello"],
#     ["this", "is", "a", "test"],
#     ["STOP", "ignore", "this", "line"],
#     ["should", "not", "be", "processed"]
# ]
# res=count_freq(paragraph)
# print(res)


#program 2
# def check_winner(board):
#     for row in board:
#         if row==["","",""]:
#             continue
#         if row[0]==row[1]==row[2]!="": 
#             return row[0]
#     for col in range(3):
#         if board[0][col]==board[1][col]==board[2][col]!="":
#             return board[0][col]
#     if board[0][0]==board[1][1]==board[2][2]!="":
#         return board[0][0]
#     if board[0][2]==board[1][1]==board[2][0]!="":
#         return board[0][2]
#     return "Draw"

        
# board = [
#     ["X", "O", "X"],
#     ["O", "X", ""],
#     ["O", "", "X"]
# ]

# res=check_winner(board)
# print(res)





#17/06/25
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

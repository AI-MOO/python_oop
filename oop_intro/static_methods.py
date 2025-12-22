# class BankAccount:
#     MIN_BALANCE = 100  # Class/static attribute, minimum balance requirement

#     def __init__(self, owner, balance=0):
#         self.owner = owner  # Instance attribute
#         self.balance = balance  # Instance attribute

#     # Instance method
#     def deposit(self, amount):
#         """Add amount to the account balance."""
#         if amount > 0:
#             self.balance += amount
#             print(f"{self.owner}'s new balance: ${self.balance}")
#         else:
#             print("Deposit amount must be positive.")

#     # Static method
#     @staticmethod
#     def is_valid_interest_rate(rate):
#         """Check if the interest rate is within a valid range (0 to 5%)."""
#         return 0 <= rate <= 5


# # Example usage
# account = BankAccount("Alice", 500)

# # Using instance method
# account.deposit(200)  # Output: Alice's new balance: $700

# # Using static method
# print(BankAccount.is_valid_interest_rate(3))  # Output: True
# print(BankAccount.is_valid_interest_rate(10))  # Output: False

# Example:


# class Person:
#     def __init__(self, name, email, address) -> None:
#         self.name = name  # public attribute
#         self._email = email  # protected attribute
#         self.__home_address = address  # private attribute

#     def print_details(self):
#         print(
#             f"Name: {self.name}; Email: {self._email}; Address: {self.__home_address}"
#         )


# person = Person("danny", "danny@gmail.com", "200 Springfield way, UK")
# person.print_details()  # Name: danny; Email: danny@gmail.com; Address: 200 Springfield way, UK

# print(person.name)  # danny
# print(person._email)  # danny@gmail.com (but we are not supposed to do this!)
# print(
#     person.__home_address
# )  # AttributeError: 'Person' object has no attribute '__home_address'




################################## protected method vs private method ##################################
class BankAccount:
    MIN_BALANCE = 100  # Class/static attribute, minimum balance requirement

    def __init__(self, owner, balance):
        self.owner = owner  # Instance attribute
        self.balance = balance  # Instance attribute

    def deposit(self, amount):
        """Add amount to the account balance."""
        if self._is_valid_amount(amount):
            self.balance += amount
            self.__log_transaction("Deposit", amount)    
        else:
            print("Deposit amount must be positive.")
    
    # protected method 
    def _is_valid_amount(self, amount):
        """Check if the amount is positive."""
        return amount > 0
    
    # private method
    def __log_transaction(self, transaction_type, amount):
        """Log the transaction details."""
        print(f"Transaction: {transaction_type} of amount ${amount}, the new balance: ${self.balance}")
        
    @staticmethod
    def is_valid_interest_rate(rate):
        """Check if the interest rate is within a valid range (0 to 5%)."""
        return 0 <= rate <= 5
    
# Example usage
account_1 = BankAccount("Alice", 500)
account_1.deposit(200)  # Output: Transaction: Deposit of amount $200,

print(account_1._is_valid_amount(-50))  # Output: True
# account_1.__log_transaction("Test", 50)  # AttributeError: 'BankAccount' object has no attribute '__log_transaction'
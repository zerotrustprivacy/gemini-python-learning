# Solution: OOP — Classes and Objects

class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height
    def area(self) -> float:
        return self.width * self.height
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance
    def deposit(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("amount must be non-negative")
        self.balance += amount
    def withdraw(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("amount must be non-negative")
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount
    def get_balance(self) -> float:
        return self.balance

class Student:
    def __init__(self, first: str, last: str) -> None:
        self.first = first
        self.last = last
    def full_name(self) -> str:
        return f"{self.first} {self.last}"
    def rename(self, first: str, last: str) -> None:
        self.first = first
        self.last = last

class Counter:
    def __init__(self, start: int = 0) -> None:
        self.value = start
    def increment(self) -> None:
        self.value += 1
    def decrement(self) -> None:
        self.value -= 1
    def get_value(self) -> int:
        return self.value
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print(f"Addition: {self.num1 + self.num2}")

    def subtract(self):
        print(f"Subtraction: {self.num1 - self.num2}")

    def multiply(self):
        print(f"Multiplication: {self.num1 * self.num2}")

    def divide(self):
        if self.num2 != 0:
            print(f"Division: {self.num1 / self.num2}")
        else:
            print("Cannot divide by zero")

calc = Calculator(10, 5)
calc.add()
calc.subtract()
calc.multiply()
calc.divide()
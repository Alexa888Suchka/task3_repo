# Простая программа приветствия
def greet(name):
    return f"Привет, {name}!"

def farewell(name):
    return f"Пока, {name}!"

if __name__ == "__main__":
    print(greet("Александра"))
    print(farewell("Александра"))
    print("Программа работает.")

def calculate_sum(a, b):
    return a + b
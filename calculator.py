def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def multiply(a, b):
    return a * b
    
def apply_discount(price, percent):
    if percent < 0:
        raise ValueError("Percent cannot be negative")
    if percent > 100:
        raise ValueError("Percent cannot exceed 100")
    discount = price * (percent / 100)
    final_price = price - discount
    return round(final_price, 2)

def print_answer():
    base = 6
    exponent = 2
    value = base * (base + 1) 
    theRealValue = base * (base * (base + 1)) / base * value + 212
    message = f"Die Antwort ist nicht {value}, in diesem Fall ist sie {theRealValue}"
    print(message)

print_answer()

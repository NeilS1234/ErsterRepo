try:
    number = int(input("Please enter a number: "))
    print(1 / number)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Enter only numbers.")
finally:
    print("Do some cleanup here.")
    

try:
    num = int(input("Enter a number:"))
    result = 10 / num
except ValueError:
    print("That's not a avalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("result:", result)
finally:
    print("Execution complete")                
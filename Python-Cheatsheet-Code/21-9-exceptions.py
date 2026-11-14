"""9. Exceptions"""

try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Number cannot be zero.")
else:
    print("Result:", result)  # runs if no exception occurred
finally:
    print("Finished.")        # runs whether an error occurred or not

try:
    x = int(input("Enter x: "))
    ans = 10/x

except ZeroDivisionError:
    print("Divided by zero not allowed")

except ValueError:
    print("Invalid Input")

else:
    print(f"ans = {ans}")

finally:
    print("End of program")
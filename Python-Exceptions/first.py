# Difference between syntax error and exception:
# a syntax error is a problem with the code
# an exception is a problem that occurs while the program is running

while True:  # the loop keeps going till it breaks
    try:
        number = int(input("whats your fav number"))
        print(18/number)
        break
    except ValueError: # code that executes if there's a value error
        print("Make sure and enter a number")
    except ZeroDivisionError: # code that executes if you try to divide by zero
        print("dont pick zero")
    finally:    # the finally occurs after the code is finished running
        print("loop complete")

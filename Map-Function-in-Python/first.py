# map is a function that runs a function through the values in a list

income = [10, 30, 75]

def double_money(dollars):
    return dollars * 2

new_income = list(map(double_money, income)) # goes through income list and runs the function through the list
print(new_income)

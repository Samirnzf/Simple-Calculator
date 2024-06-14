
def multiply_numbers(a, b):
    return a * b


def divide_numbers(a, b):
    return a / b


def subtract_numbers(a, b):
    return a - b


def add_numbers(a, b):
    return a + b


def result_is_int(result_):
    if result_.is_integer():
        return int(result_)
    else:
        return f'{result_:.2f}'


print("Select operation.")
print(" 1. Multiply numbers\n"
      " 2. Divide numbers\n"
      " 3. Subtract\n"
      " 4. Add numbers\n"
      " 5. Exit")

while True:
    command = input("Enter a command(1/2/3/4): ")
    if command in ('1', '2', '3', '4'):
        try:
            first_number = float(input("Enter first number: "))
            second_number = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please try again.")
            continue

    if command == '1':
        result = multiply_numbers(first_number, second_number)
        print(f"{first_number} * {second_number} = {result_is_int(result)}")
    elif command == '2':
        if first_number == 0 or second_number == 0:
            print('Error! Division by zero.')
        else:
            result = divide_numbers(first_number, second_number)
            print(f"{first_number} / {second_number} = {result_is_int(result)}")
    elif command == '3':
        result = subtract_numbers(first_number, second_number)
        print(f"{first_number} - {second_number} = {result_is_int(result)}")
    elif command == '4':
        result = add_numbers(first_number, second_number)
        print(f"{first_number} + {second_number} = {result_is_int(result)}")

    another_calculation = input("Let's do another calculation? (y/n): ")
    if another_calculation == 'no' or another_calculation == 'n':
        print('\nThank you for using calc.py!')
        exit()
    elif another_calculation == 'yes' or another_calculation == 'y':
        continue
    else:
        print("Invalid input")

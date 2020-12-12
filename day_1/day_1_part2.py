# Leer la entrada desde un archivo txt
#input_file = open("input.txt", "r")
input_file = open("input2.txt", "r")

expense_report = input_file.readlines()
input_file.close()

# Eliminar los saltos de línea y convertir los datos de string a entero
for index, number in enumerate(expense_report):
    expense_report[index] = number.replace("\n", "")
    expense_report[index] = int(number)

# Ordenar los números en la lista
expense_report.sort()

# Intento 1
def find_numbers_1(expense_report):
    first_index = 0
    last_index = len(expense_report) - 1
    first_number = expense_report[first_index]
    last_number = expense_report[last_index]
    target = 2020

    while first_number != last_number:
        for middle_number in expense_report:
            is_not_duplicate = (first_number != middle_number) and (middle_number != last_number)
            if is_not_duplicate:
                result = first_number + middle_number + last_number
                if result < target:
                    first_index += 1
                    first_number = expense_report[first_index]
                elif result > target:
                    last_index -= 1
                    last_number = expense_report[last_index]
                else:
                    product_numbers = first_number * last_number * middle_number
                    return first_number, middle_number, last_number, result, product_numbers
            else:
                continue

def find_numbers(expense_report):
    target = 2020
    for first_number in expense_report:
        for middle_number in expense_report:
            for last_number in expense_report:
                is_not_duplicate = (first_number != middle_number) and (first_number != last_number) and (middle_number != last_number)
                if is_not_duplicate:
                    result = first_number + middle_number + last_number
                    if result == target:
                        product_numbers = first_number * last_number * middle_number
                        return first_number, middle_number, last_number, result, product_numbers

#Calcular la multiplicación de ambos números
#product_numbers = first_number * last_number * middle_number
# print(first_number)
# print(middle_number)
# print(last_number)
# print(product_numbers)
print(find_numbers(expense_report))
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

first_index = 0
last_index = len(expense_report) - 1
first_number = expense_report[first_index]
last_number = expense_report[last_index]
target = 2020

# Recorrer la lista de números desde los extremos
# Si la suma es mayor que el objetivo, correr el 
# límite superior en 1 hacia la izquierda (y viceversa
# si es menor)
while first_number != last_number:
    result = first_number + last_number
    if result > target:
        last_index -= 1
        last_number = expense_report[last_index]
    elif result < target:
        first_index += 1
        first_number = expense_report[first_index]
    else:
        break

#Calcular la multiplicación de ambos números
product_numbers = first_number * last_number
print(first_number)
print(last_number)
print(product_numbers)
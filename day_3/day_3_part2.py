#map_file = open("input.txt", "r")
map_file = open("input2.txt", "r")
map_info = map_file.readlines()
map_file.close()

for index, line in enumerate(map_info):
    map_info[index] = line.replace("\n", "")

def count_trees(map_info, right_movement, down_movement):
    rows = len(map_info)
    cols_ratio = 1 + right_movement * (rows - 1)

    # Multiplicar el patron hasta que la diagonal llegue
    # hasta la última fila
    for index, row in enumerate(map_info):
        cols = len(row)
        row_content = row
        while cols < cols_ratio:
            map_info[index] += row_content
            cols = len(map_info[index])

    trees_number = 0
    column = 0
    tree_symbol = "#"

    for index, row in enumerate(map_info):
        if index % down_movement == 0:
            if row[column] == tree_symbol:
                trees_number += 1
            column += right_movement

    return trees_number

case_1 = count_trees(map_info, 1, 1)
case_2 = count_trees(map_info, 3, 1)
case_3 = count_trees(map_info, 5, 1)
case_4 = count_trees(map_info, 7, 1)
case_5 = count_trees(map_info, 1, 2)
result = case_1 * case_2 * case_3 * case_4 * case_5
print("Right 1, down 1: ", case_1)
print("Right 3, down 1: ", case_2)
print("Right 5, down 1: ", case_3)
print("Right 7, down 1: ", case_4)
print("Right 1, down 2: ", case_5)
print("Result: ", result)
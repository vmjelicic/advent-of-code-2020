#map_file = open("input.txt", "r")
map_file = open("input2.txt", "r")
map_info = map_file.readlines()
map_file.close()

for index, line in enumerate(map_info):
    map_info[index] = line.replace("\n", "")

rows = len(map_info)
#cols = len(map_info[0])

# Relación cols = 1 + 3 * (rows - 1)
cols_ratio = 1 + 3 * (rows - 1)

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

for row in map_info:
    if row[column] == tree_symbol:
        trees_number += 1
    column += 3

print(trees_number)
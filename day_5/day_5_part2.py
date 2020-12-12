import math

#boarding_pass_file = open("input.txt", "r")
boarding_pass_file = open("input2.txt", "r")
boarding_pass_info = boarding_pass_file.read()
boarding_pass_info = boarding_pass_info.split("\n")

busy_numbers = []


for boarding_pass in boarding_pass_info:
    row_numbers = [x for x in range(0, 128)]
    column_numbers = [x for x in range(0, 8)]
    row_code = boarding_pass[:7]
    column_code = boarding_pass[7:]
    for character in row_code:
        if character == "F":
            limit = math.floor(len(row_numbers) / 2)
            row_numbers = row_numbers[:limit]
        elif character == "B":
            limit = math.ceil(len(row_numbers) / 2)
            row_numbers = row_numbers[limit:]
    row = row_numbers[0]
    for character in column_code:
        if character == "L":
            limit = math.floor(len(column_numbers) / 2)
            column_numbers = column_numbers[:limit]
        elif character == "R":
            limit = math.ceil(len(column_numbers) / 2)
            column_numbers = column_numbers[limit:]
    column = column_numbers[0]
    seat_id = row * 8 + column
    busy_numbers.append(seat_id)

busy_numbers.sort()
count = 0

paso = min(busy_numbers)
for number in busy_numbers:
    if paso not in busy_numbers:
        print("Side ID: ", paso)
        break
    paso += 1

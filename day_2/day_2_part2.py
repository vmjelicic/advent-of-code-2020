#passwords_file = open("input.txt", "r")
passwords_file = open("input2.txt", "r")
passwords_info = passwords_file.readlines()
passwords_file.close()

passwords_db = []

for line in passwords_info:
    line_list = line.split(" ")
    range_char = line_list[0].split("-")
    new_password = dict(
        password = line_list[2].replace("\n", ""),
        char = line_list[1][0],
        first_pos = int(range_char[0]),
        second_pos = int(range_char[1])
    )
    passwords_db.append(new_password)


def is_valid_password(word, char, first_pos, second_pos):
    first_pos_test = word[first_pos - 1] == char
    second_pos_test = word[second_pos - 1] == char
    # xor
    if (first_pos_test + second_pos_test) == 1:
        return True
    else:
        return False


def count_valid_passwords(passwords_list):
    valid_passwords = 0
    for line in passwords_list:
        password = line["password"]
        char = line["char"]
        first_pos = line["first_pos"]
        second_pos = line["second_pos"]
        is_valid = is_valid_password(password, char, first_pos, second_pos)
        if is_valid:
            valid_passwords += 1
    return valid_passwords

result = count_valid_passwords(passwords_db)
print(result)
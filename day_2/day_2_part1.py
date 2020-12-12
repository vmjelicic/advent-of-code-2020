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
        min_char = int(range_char[0]),
        max_char = int(range_char[1])
    )
    passwords_db.append(new_password)

def count_char(word, char):
    result = 0
    for character in word:
        if character == char:
            result += 1
    return result

def count_valid_passwords(passwords_list):
    valid_passwords = 0
    for line in passwords_list:
        password = line["password"]
        char = line["char"]
        min_char = line["min_char"]
        max_char = line["max_char"]
        char_number = count_char(password, char)
        if min_char <= char_number <= max_char:
            valid_passwords += 1
    return valid_passwords

result = count_valid_passwords(passwords_db)
print(result)
passport_file = open("input.txt", "r")
#passport_file = open("input2.txt", "r")
passport_info = passport_file.read()
passport_file.close()

passport_info = passport_info.split("\n\n")
passports = []
for index, passport in enumerate(passport_info):
    passport_info[index] = passport.replace("\n", " ")
    new_passport_list = passport_info[index].split(" ")
    new_passport = {}
    for field in new_passport_list:
        key = field[0:3]
        value = field[4:]
        new_passport[key] = value
    passports.append(new_passport)

passport_fields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
] # "cid" queda como opcional

valid_passports = 0

for passport in passports:
    valid_fields = 0
    for passport_field in passport_fields:
        if passport_field in passport.keys():
            valid_fields += 1
    if valid_fields == len(passport_fields):
        valid_passports += 1

print("Valid passports: ", valid_passports)
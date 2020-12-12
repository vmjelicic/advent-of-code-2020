import re

#passport_file = open("input.txt", "r")
passport_file = open("input2.txt", "r")
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

    try:
        if 1920 <= int(passport["byr"]) <= 2002:
            valid_fields += 1
        if 2010 <= int(passport["iyr"]) <= 2020:
            valid_fields += 1
        if 2020 <= int(passport["eyr"]) <= 2030:
            valid_fields += 1
        if passport["hgt"][len(passport["hgt"])-2:len(passport["hgt"])] == "cm":
            if 150 <= int(passport["hgt"][0:3]) <= 193:
                valid_fields += 1
        if passport["hgt"][len(passport["hgt"])-2:len(passport["hgt"])] == "in":
            if 59 <= int(passport["hgt"][0:2]) <= 76:
                valid_fields += 1
        if re.search(r"^#([0-9]|[a-f]){6}$", passport["hcl"]):
            valid_fields += 1
        if re.search(r"^(amb|blu|brn|gry|grn|hzl|oth)$", passport["ecl"]):
            valid_fields += 1
        if re.search(r"^[0-9]{9}$", passport["pid"]):
            valid_fields += 1
    except:
        continue

    
    if valid_fields == len(passport_fields):
        valid_passports += 1

print("Valid passports: ", valid_passports)
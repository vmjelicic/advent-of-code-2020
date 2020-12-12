rules_file = open("input.txt", "r")
#rules_file = open("input2.txt", "r")
rules_info = rules_file.read()
rules_info = rules_info.split("\n")
rules_file.close()

rules = {}
print(rules_info)
# [name1] [name2] bags contain [number] [name3] [name4], ([number] [name3] [name4]){inf}
for rule in rules_info:
    rule = rule.split(" ")
    key_rule = rule[0] + "_" + rule[1]
    rules[key_rule] = {}




"""rules = {
    "light_red": {
        "bright_white": 1,
        "muted_yellow": 2
    },
    "dark_orange": {
        "bright_white": 3,
        "muted_yellow": 4
    },
    "bright_white": {
        "shiny_gold": 1
    },
    "muted_yellow": {
        "shiny_gold": 2,
        "faded_blue": 9
    },
    "shiny_gold": {
        "dark_olive": 1,
        "vibrant_plum": 2
    },
    "dark_olive": {
        "faded_blue": 3,
        "dotted_black": 4
    },
    "vibrant_plum": {
        "faded_blue": 5,
        "dotted_black": 6
    },
    "faded_blue": {},
    "dotted_black": {}
}"""
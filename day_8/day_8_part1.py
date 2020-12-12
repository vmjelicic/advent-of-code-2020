instructions_file = open("input.txt", "r")
#instructions_file = open("input2.txt", "r")
instructions_info = instructions_file.read()
instructions_file.close()
instructions_info = instructions_info.split("\n")

rep_lines = []
for index in range(len(instructions_info)):
    rep_lines.append(0)

acc = 0
index = 0
repetition_count = rep_lines[0]

while repetition_count < 2:
    instruction = instructions_info[index].split(" ")
    instruction_type = instruction[0]
    instruction_num = int(instruction[1])
    if instruction_type == "acc":
        index += 1
        acc += instruction_num
    elif instruction_type == "jmp":
        index += instruction_num
    elif instruction_type == "nop":
        index += 1
    rep_lines[index] += 1
    repetition_count = rep_lines[index]

print("Accumulator: ", acc)
print(repetition_count)
instructions_file = open("input.txt", "r")
#instructions_file = open("input2.txt", "r")
instructions_info = instructions_file.read()
instructions_file.close()
instructions_info = instructions_info.split("\n")

def execute_instruction(instructions_info):
    rep_lines = []
    for index in range(len(instructions_info)):
        rep_lines.append(0)

    acc = 0
    index = 0
    repetition_count = rep_lines[0]

    while (repetition_count < 2) or (index < len(instructions_info)):
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

        print("Rep_count: {}, Instructions_no: {}, index: {}, acc: {}".format(
            repetition_count, len(instructions_info), index, acc
        ))
        return acc, repetition_count


def find_index_instruction(instruction_info):
    index_list = []
    for index in range(len(instructions_info)):
        instruction = instructions_info[index].split(" ")
        instruction_type = instruction[0]
        if (instruction_type == "jmp") or (instruction_type == "nop"):
            index_list.append(index)
    return index_list


def change_instruction(instruction_info, index_list, instruction_num):
    instructions = instruction_info
    index = index_list[instruction_num]
    instruction = instructions[index].split(" ")[0]
    if instruction == "jmp":
        instructions[index].replace("jmp", "nop")
    elif instruction == "nop":
        instructions[index].replace("nop", "jmp")
    return instructions
    

def find_corrupted_instruction(instructions_info):
    index_list = find_index_instruction(instructions_info)
    repetition_count = 2
    index_instruction = 0
    while repetition_count == 2:
        instructions_test = change_instruction(
            instructions_info, index_list, index_instruction
        )
        acc, repetition_count = execute_instruction(instructions_test)
        print("Repetition: {}, acc: {}".format(repetition_count, acc))
        index_instruction += 1
    return acc

print(find_corrupted_instruction(instructions_info))
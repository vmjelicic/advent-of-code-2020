#answers_file = open("input.txt", "r")
answers_file = open("input2.txt", "r")
answers_info = answers_file.read()
answers_info = answers_info.split("\n\n")

total_questions = 0

for answer in answers_info:
    questions_number = 0
    questions_answered = []
    answer = answer.replace("\n", "")
    for question in answer:
        if question not in questions_answered:
            questions_answered.append(question)
            questions_number += 1
    #print(questions_number)
    total_questions += questions_number
print(total_questions)

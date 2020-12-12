#answers_file = open("input.txt", "r")
answers_file = open("input2.txt", "r")
answers_info = answers_file.read()
answers_info = answers_info.split("\n\n")

total_questions = 0

for answer in answers_info:
    valid_questions = 0
    questions_answered = {}
    persons_number = len(answer.split("\n"))
    answer = answer.replace("\n", "")
    for question in answer:
        if question not in questions_answered:
            questions_answered[question] = 1
        else:
            questions_answered[question] += 1
    for question in questions_answered.keys():
        if questions_answered[question] == persons_number:
            valid_questions += 1        
    #print(valid_questions)
    total_questions += valid_questions
print(total_questions)
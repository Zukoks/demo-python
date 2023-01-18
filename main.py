# Счетчик правильных ответов
correct_answers = 0

# Приветствие
print("Привет! Предлагаю проверить свои знания английского!")
user_name = input("Расскажи, как тебя зовут?\n")
print(f"Привет, {user_name}, начинаем тренировку!")

# Вопрос №1
question_1 = "Вопрос: My name __ Vova\n"
correct_answer_1 = "is"
user_answer_1 = input(question_1)
if user_answer_1 == correct_answer_1:
    correct_answers += 1
    print("Ответ верный!\nВы получаете 10 баллов!")
else:
    print(f"Неправильно. Правильный ответ: {correct_answer_1}")

# Вопрос №2
question_2 = "Вопрос: I __ a coder\n"
correct_answer_2 = "am"
user_answer_2 = input(question_2)
if user_answer_2 == correct_answer_2:
    correct_answers += 1
    print("Ответ верный!\nВы получаете 10 баллов!")
else:
    print(f"Неправильно. Правильный ответ: {correct_answer_2}")

# Вопрос №3
question_3 = "Вопрос: I live __ Moscow\n"
correct_answer_3 = "in"
user_answer_3 = input(question_3)
if user_answer_3 == correct_answer_3:
    correct_answers += 1
    print("Ответ верный!\nВы получаете 10 баллов!")
else:
    print(f"Неправильно. Правильный ответ: {correct_answer_3}")

# Количество баллов пользователя
user_score = correct_answers * 10
# Количество процентов
user_percentage = int(correct_answers/3*100)

# Результат опроса
print(
    f"\nВот и все, {user_name}!\n"
    f"Вы ответили на {correct_answers} вопросов из 3 верно.\n"
    f"Вы заработали {user_score} баллов.\n"
    f"Это {user_percentage} процентов."
)
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Переводим множество студентов в список и сортируем его
students_list = list(students)
list.sort(students_list)

# Создаем справочник со средними оценками
sr_bal_students = {students_list[0]: sum(grades[0])/len(grades[0])}

# Определяем длину списка
dlina = len(students_list)

# Добавляем в справочник остальные элементы
i = 1
for i in range(dlina):
    sr_bal_students.update({students_list[i]: sum(grades[i]) / len(grades[i])})

# Результат
print(sr_bal_students)
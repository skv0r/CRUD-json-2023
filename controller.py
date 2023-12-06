#сюда поступают ответы действия пользователя
#отсылает запрос в model и view
from model import IsInt
from components.students.students_controller import AddStudent, FindExamResult, FindStudent, EditStudent, DeleteStudent, ShowStudent
from components.directions.directions_controller import AddDirections, FindDirection, EditDirection, DeleteDirection

def FuncEdit(student):
    second_step = str(input(f'Напишите номер действия для управления БД:\n1 - Изменить имя\n2 - Изменить СНИЛС\n3 - Изменить баллы за экзамен\n'))
    if (IsInt(second_step) == True) and (1 <= int(second_step) <= 3):
        EditStudent(student, second_step)
    else:
        return FuncEdit(student)



def FuncDirection(second_step):
    if (IsInt(second_step) == True) and (1 <= int(second_step) <= 4):
        FuncDoSecond(second_step)
    else:
        return FuncDirection(second_step)

def FuncDoSecond(num):
    if int(num) == 1:
        direction_name = str(input(f'Ввведите имя направления\n'))
        direction_id = str(input(f'Ввведите номер направления\n'))
        points_2023 = str(input(f'Ввведите мин. балл за 2023\n'))
        year2022 = str(input(f'Ввведите мин. балл за 2022\n'))
        year2021 = str(input(f'Ввведите мин. балл за 2021\n'))
        year2020 = str(input(f'Ввведите мин. балл за 2021\n'))
        AddDirections(direction_name, direction_id, points_2023, year2022, year2021, year2020)
        print("Направление успешно добавлено")
    if int(num) == 2:
        direction_id = str(input(f"Введите номер направления\n"))
        direction = FindDirection(direction_id)
        print(f'Название: {direction["direction"]}\nНомер: {direction["direction_id"]}\nМин.Балл за 2023: {direction["points_2023"]}\nСредний мин.балл за последние годы: {(int(direction["midrange_points"]["2022"])+int(direction["midrange_points"]["2021"])+int(direction["midrange_points"]["2021"]))//3}')
    if int(num) == 3:
        direction_id = str(input(f"Введите номер направления\n"))
        EditDirection(FindDirection(direction_id))
    if int(num) == 4:
        direction_id = str(input(f"Введите номер направления\n"))
        DeleteDirection(FindDirection(direction_id))


def FuncDo(num):
    if int(num) == 1:
        name =  str(input(f'Ввведите имя студента:\n'))
        document = str(input(f'Введите номер СНИЛС слитно:\n'))
        exam_result = str(input(f'Введите сумму баллов за экзамен:\n'))
        AddStudent(name, document, exam_result)
        return 'Студент успешно добавлен'
    elif int(num) == 2:
        document = str(input(f'Введите номер СНИЛС слитно:\n'))
        return FindExamResult(document)
    elif int(num) == 3: 
        document = str(input(f'Введите номер СНИЛС слитно:\n'))
        FuncEdit(FindStudent(document))
        return 'Изменения успешно применены'
    elif int(num) == 4:
        document = str(input(f'Введите номер СНИЛС слитно:\n'))
        DeleteStudent(FindStudent(document))
        return 'Студент успешно удален'
    elif int(num) == 5:
        second_step = str(input(f'Напишите номер действия для управления БД:\n1 - Добавить направление\n2 - Узнать информацию по направлениям\n3 - Редактировать направление\n4 - Удалить направление\n'))
        FuncDirection(second_step)
        return ''
    elif int(num) == 6:
        docs = ShowStudent('creds.json')["documents"]
        print(f'Документы на: 10 баллов - {docs[0]["specialdocs"]["10"]}\nДокументы на: 7 баллов - {docs[0]["specialdocs"]["7"]}\nДокументы на: 5 баллов - {docs[0]["specialdocs"]["5"]}\nДокументы на: 3 баллов - {docs[0]["specialdocs"]["3"]}\nДокументы на: 1 баллов - {docs[0]["specialdocs"]["1"]}\nДокументы на поступление без экзаменов - {docs[0]["autodocs"]["without_exam"]}\n')
        return ""
    

#сюда поступают ответы действия пользователя
#отсылает запрос в model и view
from model import AddStudent, FindExamResult, IsInt, FindStudent, EditStudent, DeleteStudent, ShowStudent

def FuncEdit(student):
    second_step = str(input(f'Напишите номер действия для управления БД:\n1 - Изменить имя\n2 - Изменить СНИЛС\n3 - Изменить баллы за экзамен\n'))
    if (IsInt(second_step) == True) and (1 <= int(second_step) <= 3):
        return EditStudent(student)
    else:
        return FuncEdit(student)
            



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
    elif int(num) == 3: #СДЕЛАТЬ
        document = str(input(f'Введите номер СНИЛС слитно:\n'))
        FuncEdit(FindStudent(document))
    elif int(num) == 4:
        document = str(input(f'Введите номер СНИЛС слитно:\n'))
        DeleteStudent(FindStudent(document))
        return 'Студент успешно удален'

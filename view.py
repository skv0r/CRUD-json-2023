#выдача меню кнопок пользователю
from model import IsInt, CreatingBaseStudents
from controller import FuncDo


def MainView():
    first_step = str(input(f'Напишите номер действия для управления БД:\n1 - Добавить студента\n2 - Узнать баллы по снилс\n3 - Изменить данные стундента\n4 - Удалить студента\n5 - Узнать информацию по направлениям\n6 - Узнать бонусные документы\n'))
    if (IsInt(first_step) == True) and (1 <= int(first_step) <= 6):
        return FuncDo(first_step)
    else:
        MainView()

print(MainView())




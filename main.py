import json

default = 0 #local const


def AddStundent(data, file_name):
    data = json.dumps(data)
    data = json.loads(str(data))

    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def FindStudent(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)


    
'''   
    
data = {
    'student': []
}

data['student'].append({
    'name': 'Artem',
    'document_id': 15968025712,
    'exam_result': 271
})
data['student'].append({
    'name': 'Anton',
    'document_id': 15968025711,
    'exam_result': 279
})

AddStundent(data, 'base.json')
student = FindStudent('base.json')
for student in student['student']:
    if student.get('exam_result') > 275:
        print(student)
'''
def ChooseNum(counter):
    try:
        if counter == 0:
            num_do = int(input(f'Напишите номер действия для управления БД:\n1 - Добавить студента\n2 - Узнать баллы по снилс\n3 - Изменить данные стундента\n4 - Удалить студента\n'))
            if num_do not in range(1,5):
                int('these for except')
            else:
                return num_do
        elif counter > 0:
            num_do = int(input(f'Вы ввели неправильно номер, попробуйте ввести заного\n')) 
            if num_do not in range(1,5):
                int('these for except')
            else:
                return num_do
    except:
        counter += 1
        return ChooseNum(counter)

def ChooseFunc(counter):
    try:
        if counter == 0:
            num_do = int(input(f'Напишите номер действия для управления БД:\n1 - Изменить имя\n2 - Изменить СНИЛС\n3 - Изменить баллы за экзамен\n'))
            if num_do not in range(1,4):
                int('these for except')
            else:
                return num_do
        elif counter > 0:
            num_do = int(input(f'Вы ввели неправильно номер, попробуйте ввести заного\n')) 
            if num_do not in range(1,4):
                int('these for except')
            else:
                return num_do
    except:
        counter += 1
        return ChooseNum(counter)

order = ChooseNum(default)
if order == 1: #ready
    name =  str(input(f'Ввведите имя студента:\n'))
    document = str(input(f'Введите номер СНИЛС слитно:\n'))
    exam_result = input(f'Введите сумму баллов за экзамен:\n')
    data = FindStudent('base.json')
    data['student'].append({
        'name': f'{name}',
        'document_id': f'{document}',
        'exam_result': exam_result
    })
    AddStundent(data, 'base.json')
elif order == 2: #полностью готова кнопка 2
    counter = 0
    doc_id = str(input(f'Ввведите СНИЛС слитно\n'))
    student = FindStudent('base.json')
    for document in student['student']:
        if document.get('document_id') == doc_id:
            counter +=1
            result = document.get('exam_result')
            print(f'Результат = {result}')
    if counter == 0:
        print(f'Студент со СНИЛС {doc_id} не найден')


elif order == 3: #ready
    counter = 0
    doc_id = str(input(f'Ввведите СНИЛС слитно\n'))
    string_student = 0

    student = FindStudent('base.json')
    for document in student['student']:
        string_student +=1
        if document.get('document_id') == doc_id:
            counter +=1
            order_func = ChooseFunc(default)
            if order_func == 1: #ready
                new_name = input(f'Введите новое имя:\n')
                (student['student'])[string_student-1]['name'] = new_name
                AddStundent(student, 'base.json')
            if order_func == 2: #ready
                new_doc = input(f'Введите новый номер СНИЛС:\n')
                (student['student'])[string_student-1]['document_id'] = new_doc
                AddStundent(student, 'base.json')
            if order_func == 3:
                new_exam = input(f'Введите результат экзаменов:\n')
                (student['student'])[string_student-1]['exam_result'] = new_exam
                AddStundent(student, 'base.json')
            
    if counter == 0:
        print(f'Студент со СНИЛС {doc_id} не найден')
elif order == 4:
    counter = 0
    string_student = 0
    #doc_id = str(input(f'Ввведите СНИЛС слитно\n'))

    doc_id = '1592570917'

    student = FindStudent('base.json')
    for document in student['student']:
        string_student += 1
        if document.get('document_id') == doc_id:
            counter +=1
            del student['student'][string_student-1]
            AddStundent(student, 'base.json') 
    if counter == 0:
        print(f'Студент со СНИЛС {doc_id} не найден')
    



#user -> view -> controller -> module -> base 
#base -> module -> controller -> view -> user
import json

class Base:
    def __init__(self):
        self.students = {
            "students": []
        }

class Student:
    def __init__(self, name, document, exam_result):
        self.data = {
            "name": f'{name}',
            "document_id": f'{document}',
            "exam_result": f'{exam_result}'
        }

constlen = len(Student(1,1,1).data) #enter if have new data in Student

def BaseStudent(data, file_name):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def ShowStudent(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)


def CreatingBaseStudents(name, doc, exam):
    base = Base()
    student = Student(name, doc, exam)
    base.students["students"].append(student.data)
    BaseStudent( base.students, 'creds.json')

def AddStudent(name, doc, exam):
    base = ShowStudent('creds.json')
    student = Student(name, doc, exam)
    base["students"].append(student.data)
    BaseStudent( base, 'creds.json')

def FindStudent(doc):
    try:
        counter = 0
        base = ShowStudent('creds.json')
        for student in base["students"]:
            if student["document_id"] == doc:
                counter +=1
                return student
        if counter == 0:
            int('a')
    except:
        print('Такой студент не найден, попробуйте еще раз!')
        doc = str(input())
        return FindStudent(doc)


def FindExamResult(doc):
    return FindStudent(doc)["exam_result"]

def DeleteStudent(student):
    string = 0
    base = ShowStudent('creds.json')
    for student in base['students']:
        string +=1
        del base['students'][string-1]
        BaseStudent(base, 'creds.json')

def EditStudent(student, number_step):
    counter = 0
    base = ShowStudent('creds.json')
    for base_student in base['students']:
        counter += 1
        if base_student == student:
            if int(number_step) == 1:
                new_name = str(input(f'Введите новое имя:\n'))
                base['students'][counter-1]['name'] = new_name
                BaseStudent(base, 'creds.json')
            if int(number_step) == 2:
                new_doc = str(input(f'Введите новый СНИЛС:\n'))
                base['students'][counter-1]['document_id'] = new_doc
                BaseStudent(base, 'creds.json')
            if int(number_step) == 3:
                new_exam = str(input(f'Введите новые баллы:\n'))
                base['students'][counter-1]['exam_result'] = new_exam
                BaseStudent(base, 'creds.json')
        
    



def IsInt(str):
    try:
        int(str)
        return True
    except ValueError:
        return False





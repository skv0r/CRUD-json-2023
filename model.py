#user -> view -> controller -> module -> base 
#base -> module -> controller -> view -> user
import json

class Base:
    def __init__(self):
        self.students = {
            "students": [],
           "directions": [],
        }

class Student:
    def __init__(self, name, document, exam_result):
        self.data = {
            "name": f'{name}',
            "document_id": f'{document}',
            "exam_result": f'{exam_result}'
        }

class Directions:
    def __init__(self, name_direction, direction_id , points_2023, year2022, year2021, year2020):
        self.data = {
            "direction": f'{name_direction}',
            "direction_id": f'{direction_id}',
            "points_2023": f'{points_2023}',
            "midrange_points": {
                "2022": f'{year2022}',
                "2021": f'{year2021}',
                "2020": f'{year2020}'
            }
        }


constlen = len(Student(1,1,1).data) #enter if have new data in Student

def CreatingBaseStudents(database):
    base = Base()
    base.students["students"]
    base.students["directions"]
    BaseStudent( base.students, f'{database}')


def BaseStudent(data, file_name):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def ShowStudent(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)



def IsInt(str):
    try:
        int(str)
        return True
    except ValueError:
        return False





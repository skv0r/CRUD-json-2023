from model import Base, Directions, ShowStudent, BaseStudent

def AddDirections(name_direction, direction_id, points_2023, year2022, year2021, year2020):
    base = ShowStudent('creds.json')
    direction = Directions(name_direction, direction_id, points_2023, year2022, year2021, year2020)
    base["directions"].append(direction.data)
    BaseStudent( base, 'creds.json')


def FindDirection(direction_id):
    try:
        counter = 0
        base = ShowStudent('creds.json')
        for direction in base["directions"]:
            if direction["direction_id"] == direction_id:
                counter +=1
                return direction
        if counter == 0:
            int('a')
    except:
        print('Такое направление не найдено, попробуйте еще раз!')
        direction_id = str(input())
        return FindDirection(direction_id)

def EditDirection(direction):
    counter = 0
    base = ShowStudent('creds.json')
    for base_direction in base['directions']:
        counter += 1
        if base_direction == direction:
            direction_name = str(input(f'Ввведите имя направления\n'))
            direction_id = str(input(f'Ввведите номер направления\n'))
            points_2023 = str(input(f'Ввведите мин. балл за 2023\n'))
            year2022 = str(input(f'Ввведите мин. балл за 2022\n'))
            year2021 = str(input(f'Ввведите мин. балл за 2021\n'))
            year2020 = str(input(f'Ввведите мин. балл за 2021\n'))
            base['directions'][counter-1]['direction'] = direction_name
            base['directions'][counter-1]['direction_id'] = direction_id
            base['directions'][counter-1]['points_2023'] = points_2023
            base['directions'][counter-1]['midrange_points']['2022'] = year2022
            base['directions'][counter-1]['midrange_points']['2021'] = year2021
            base['directions'][counter-1]['midrange_points']['2020'] = year2020
            BaseStudent(base, 'creds.json')
    print("Направление успешно изменено")

def DeleteDirection(direction):
    string = 0
    base = ShowStudent('creds.json')
    for step in range(0,len(base['directions'])):
        if direction == base['directions'][string]:
            del base['directions'][string]
        else:
            string +=1
    BaseStudent(base, 'creds.json')
    print('Направление успешно удалено')
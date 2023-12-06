from model import Base, Directions, ShowStudent, BaseStudent

def AddDirections(name_direction, direction_id, points_2023, year2022, year2021, year2020):
    base = ShowStudent('creds.json')
    direction = Directions(name_direction, direction_id, points_2023, year2022, year2021, year2020)
    base["directions"].append(direction.data)
    BaseStudent( base, 'creds.json')

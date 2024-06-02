def _err(heroes_list: list):
    if len(heroes_list) == 0:
        raise ValueError("Error, empty list")


def show_name(heroes_list: list):
    _err(heroes_list=heroes_list)

    for heroe in heroes_list:
        print("Nombre: ", heroe['nombre'])


def show_name_and_height(heroes_list: list):
    _err(heroes_list=heroes_list)
    for heroe in heroes_list:
        name = heroe['nombre']
        height = heroe['altura']

        print(f"Nombre: {name}, Altura: {height}")


def get_by_value(heroes_list: list, value: str, key: str) -> tuple:
    _err(heroes_list=heroes_list)

    current_value = heroes_list[0][f'{key}']
    current_name = heroes_list[0]['nombre']
    
    for hero in heroes_list:
        if value == "min":
            if float(hero[f'{key}']) < float(current_value):
                current_value = hero[f'{key}']
                current_name = hero["nombre"]
        else:
            if float(hero[f'{key}']) > float(current_value):
                current_value = hero[f'{key}']
                current_name = hero["nombre"]

    return current_value, current_name


def get_height_average(heroes_list: list):
    _err(heroes_list=heroes_list)

    heights = 0

    for hero in heroes_list:
        heights += float(hero['altura'])

    return heights / len(heroes_list)

def get_max_and_min_weight(heroes_list: list) -> tuple:
    _err(heroes_list=heroes_list)

    max_weight, max_weight_name = get_by_value(heroes_list=heroes_list, value="max", key="peso")
    min_weight, min_weight_name = get_by_value(heroes_list=heroes_list, value="min", key="peso")

    return max_weight, max_weight_name, min_weight, min_weight_name


def get_height_identity(heroes_list: list, name: str) -> str:
    _err(heroes_list=heroes_list)

    for hero in heroes_list:
        if name == hero["nombre"]:
            return hero["identidad"]
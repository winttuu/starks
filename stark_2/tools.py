

def get_heroes_by_gender(heroes_list: list, gender: str) -> list:
    return [ hero for hero in heroes_list if hero["genero"] == gender]

def get_hero_by_attributes(heroes_list: list, gender: str, key_to_search: str, value: str) -> list:
    heroes = get_heroes_by_gender(heroes_list=heroes_list, gender=gender)

    current_value = heroes[0][f'{key_to_search}']
    current_hero = heroes[0]

    for hero in heroes:
        key = float(hero[f"{key_to_search}"])

        if value == "max":
            if key > float(current_value):
                current_value = key
                current_hero = hero
        else:
            if key < float(current_value):
                current_value = key
                current_hero = hero

    return current_hero


def get_height_average(heroes_list: list, gender: str):
    heroes = get_heroes_by_gender(heroes_list=heroes_list, gender=gender)

    height_suma = 0

    for hero in heroes:
        height_suma += float(hero["altura"])

    return height_suma / len(heroes)

def group_heroes_by_attribute(heroes_list: list, attribute: str) -> list:
    attributes_list = []
    unique_heroes = []

    for hero in heroes_list:
        if hero[f"{attribute}"] not in attributes_list:
            attributes_list.append(hero[f"{attribute}"])
            unique_heroes.append(hero)

    return unique_heroes


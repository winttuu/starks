import tools

def case_a(heroes_list: list):
    man_list = tools.get_heroes_by_gender(heroes_list=heroes_list, gender="M")
    
    for hero in man_list:
        print(f"Nombre: {hero['nombre']}")

def case_b(heroes_list: list):
    female_list = tools.get_heroes_by_gender(heroes_list=heroes_list, gender="F")
    
    for hero in female_list:
        print(f"Nombre: {hero['nombre']}")

def case_c(heroes_list: list):
    max_height_m = tools.get_hero_by_attributes(heroes_list=heroes_list, gender="M", key_to_search="altura", value="max")
    print(f"El superheroe masculino mas alto es: {max_height_m}")
    return max_height_m

def case_d(heroes_list: list):
    max_height_f = tools.get_hero_by_attributes(heroes_list=heroes_list, gender="F", key_to_search="altura", value="max")
    print(f"El superheroina femenina mas alto es: {max_height_f}")
    return max_height_f

def case_e(heroes_list: list):
    min_height_m = tools.get_hero_by_attributes(heroes_list=heroes_list, gender="M", key_to_search="altura", value="min")
    print(f"El superheroe masculino mas bajo es: {min_height_m}")
    return min_height_m

def case_f(heroes_list: list):
    min_height_f = tools.get_hero_by_attributes(heroes_list=heroes_list, gender="F", key_to_search="altura", value="min")
    print(f"La superheroina mas baja es: {min_height_f}")
    return min_height_f

def case_g(heroes_list: list):
    height_average_m = tools.get_height_average(heroes_list=heroes_list, gender="M")
    print(f"El promedio de altura masculino es: {height_average_m}")

def case_h(heroes_list: list):
    height_average_f = tools.get_height_average(heroes_list=heroes_list, gender="F")
    print(f"El promedio de altura femenino es: {height_average_f}")

def case_i(heroes_list: list):
    pass

def case_j(heroes_list: list):
    group_eyes_color = tools.group_heroes_by_attribute(heroes_list=heroes_list, attribute="color_ojos")
    print(f"Los superheroes con distinto color de ojos son: {len(group_eyes_color)}")

def case_k(heroes_list: list):
    group_hair_color = tools.group_heroes_by_attribute(heroes_list=heroes_list, attribute="color_pelo")
    print(f"Los superheroes con distinto color de pelo son: {len(group_hair_color)}")

def case_l(heroes_list: list):
    group_intelligence = tools.group_heroes_by_attribute(heroes_list=heroes_list, attribute="inteligencia")
    print(f"Los superheroes con distinta inteligencia son: {len(group_intelligence)}")

def case_m(heroes_list: list):
    group_eyes_color = tools.group_heroes_by_attribute(heroes_list=heroes_list, attribute="color_ojos")
    print(f"Los superheroes con distinto color de ojos son: {group_eyes_color}")

def case_n(heroes_list: list):
    group_hair_color = tools.group_heroes_by_attribute(heroes_list=heroes_list, attribute="color_pelo")
    print(f"Los superheroes con distinto color de pelo son: {group_hair_color}")

def case_o(heroes_list: list):
    group_intelligence = tools.group_heroes_by_attribute(heroes_list=heroes_list, attribute="inteligencia")
    print(f"Los superheroes con distinta inteligencia son: {group_intelligence}")
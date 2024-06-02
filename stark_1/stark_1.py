from data_stark_1 import lista_heroes
import tools

def menu():
    print(lista_heroes)

    while True:
        print("""
            A. Mostrar el nombre de todos los superheroes
            B. Mostrar el nombre y la altura de todos los superheroes
            C. Mostrar el superheroe mas alto
            D. Mostrar el superheroe mas bajo
            E. Mostrar la altura promedio de los superheroes
            F. Mostrar la identidad del superheroe mas bajo y mas alto.
            G. Mostrar el superheroe mas pesado y el menos pesado.
              
            X. Salir
        """)

        option = input("Escoge una opcion: ").lower()
        
        match option:
            case 'a':
                tools.show_name(heroes_list=lista_heroes)
            case 'b':
                tools.show_name_and_height(heroes_list=lista_heroes)
            case 'c':
                max_height, name_max_height = tools.get_by_value(heroes_list=lista_heroes, value="max", key="altura")
                print(f"El superheroe mas alto es: {name_max_height}. Su altura es: {max_height}")
            case 'd':
                min_height, name_min_height = tools.get_by_value(heroes_list=lista_heroes, value="min", key="altura")
                print(f"El superheroe mas bajo es: {name_min_height}. Su altura es: {min_height}")
            case 'e':
                height_avg = tools.get_height_average(heroes_list=lista_heroes)
                print(f"El promedio de altura es: {height_avg}")
            case 'f':
                max_height, name_max_height = tools.get_by_value(heroes_list=lista_heroes, value="max", key="altura")
                min_height, name_min_height = tools.get_by_value(heroes_list=lista_heroes, value="min", key="altura")

                identity_max_height = tools.get_height_identity(heroes_list=lista_heroes, name=name_max_height)
                identity_min_height = tools.get_height_identity(heroes_list=lista_heroes, name=name_min_height)

                print(f"La identidad del superheroe mas bajo es: {identity_min_height} y la identidad del mas alto es: {identity_max_height}")

            case 'g':
                max_weight, max_weight_name, min_weight, min_weight_name = tools.get_max_and_min_weight(heroes_list=lista_heroes)
                print(f"El superheroe mas pesado es: {max_weight_name} ({max_weight}), el menos pesado: {min_weight_name} ({min_weight})")
            case 'x':
                break
            case _:
                print("opcion invalida")

menu()
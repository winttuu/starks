from data_stark_2 import heroes_list
import cases

def menu():
    print("""
        A. Mostrar los nombres de todos los superheroes masculinos
        B. Mostrar los nombres de todas las superheroinas femeninas
        C. Mostrar el superhéroe más alto de género Masculino
        D. Mostrar el superhéroe más alto de género Femenino
        E. Mostrar el superhéroe más bajo de género Masculino
        F. Mostrar el superhéroe más bajo de género Femenino
        G. Mostrar la altura promedio de los superhéroes de género Masculino
        H. Mostrar la altura promedio de los superhéroes de género Femenino
        I. Mostrar cual es el nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
        J. Mostrar cuántos superhéroes tienen cada tipo de color de ojos.
        K. Mostrar cuántos superhéroes tienen cada tipo de color de pelo.
        L. Mostrar cuántos superhéroes tienen cada tipo de inteligencia
        M. Mostrar todos los superhéroes agrupados por color de ojos.
        N. Mostrar todos los superhéroes agrupados por color de pelo.
        O. Mostrar todos los superhéroes agrupados por tipo de inteligencia   
                    
        X. Salir
    """)

    option = input("Escoge una opcion: ").lower()
    return option

def app():
    print(heroes_list)

    while True:
        option = menu()
        
        match option:
            case "a":
                cases.case_a(heroes_list=heroes_list)
            case "b":
                cases.case_b(heroes_list=heroes_list)
            case "c":
               cases.case_c(heroes_list=heroes_list)
            case "d":
                cases.case_d(heroes_list=heroes_list)
            case "e":
                cases.case_e(heroes_list=heroes_list)
            case "f":
                cases.case_f(heroes_list=heroes_list)
            case "g":
                cases.case_g(heroes_list=heroes_list)
            case "h":
                cases.case_h(heroes_list=heroes_list)
            case "i":
                cases.case_i(heroes_list=heroes_list)
            case "j":
                cases.case_j(heroes_list=heroes_list)
            case "k":
                cases.case_k(heroes_list=heroes_list)           
            case "l":
                cases.case_l(heroes_list=heroes_list)                      
            case "m":
                cases.case_m(heroes_list=heroes_list)           
            case "n":
                cases.case_n(heroes_list=heroes_list)           
            case "o":
                cases.case_o(heroes_list=heroes_list)           
            case "x":
                break
            case _:
                print("Error, invalid option")


app()
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
            case "a":
                pass

menu()
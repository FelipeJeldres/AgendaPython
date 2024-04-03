agenda = {
    "Jose": 302944,
    "Mario": 829455,
    "Angel": 829405,
    "Luis": 930594,
}

consultando = True

while consultando:
    print()
    print("MI AGENDA")
    print("----------------------------")
    print("1. Consultar\n2. Añadir\n3. Modificar\n4. Borrar\n5. Salir")
    opcion = ""
    while opcion not in ("1", "2", "3", "4", "5"):
        opcion = input("-> ")

    if opcion == "1":  # Consultar
        nombre = input("Ingrese el nombre a consultar: ")
        if nombre in agenda:
            print(f"El número de {nombre} es: {agenda[nombre]}")
        else:
            print("El nombre no está en la agenda.")

    elif opcion == "2":  # Añadir
        nombre = input("Ingrese el nombre a añadir: ")
        numero = input("Ingrese el número correspondiente: ")
        agenda[nombre] = numero
        print(f"¡Se ha añadido a {nombre} en la agenda!")

    elif opcion == "3":  # Modificar
        nombre = input("Ingrese el nombre a modificar: ")
        if nombre in agenda:
            nuevo_numero = input("Ingrese el nuevo número correspondiente: ")
            agenda[nombre] = nuevo_numero
            print(f"¡Se ha modificado el número de {nombre}!")
        else:
            print("El nombre no está en la agenda.")

    elif opcion == "4":  # Borrar
        nombre = input("Ingrese el nombre a borrar: ")
        if nombre in agenda:
            del agenda[nombre]
            print(f"¡Se ha borrado a {nombre} de la agenda!")
        else:
            print("El nombre no está en la agenda.")

    elif opcion == "5":  # Salir
        consultando = False
        print("¡Hasta luego!")

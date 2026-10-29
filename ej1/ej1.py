notas = {"Villalobos": [], "Olguin": [], "Salinas": [], "Moreno": [], "Sella": []}
seguir = "si"
while seguir == "si":
    print("BIENVENIDO AL MENU DE NOTAS DE PROGRAMACION")
    print("1. Ver todas las notas")
    print("2. Ver notas por alumno")
    print("3. Cargar notas")
    print("4. Promedio")
    print("5. Salir")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        for alumno in notas:
            print("Alumno:", alumno, "- Notas:", notas[alumno])
    elif opcion == "2":
        apellido = input("Ingrese el apellido del alumno: ")
        if apellido in notas:
            print("Notas de", apellido, ":", notas[apellido])
        else:
            print("El alumno no se encuentra")
    elif opcion == "3":
        apellido = input("Ingrese el apellido del alumno a cargar: ")
        if apellido in notas:
            for i in range(1, 6):
                nota = float(input("Ingrese la nota: "))
                notas[apellido].append(nota)
            print("Notas cargadas")
        else:
            print("El alumno no se encuentra en el sistema.")
    elif opcion == "4":
        apellido = input("Ingrese el apellido del alumno: ")
        if apellido in notas:
            lista_notas = notas[apellido]
            if len(lista_notas) == 0:
                print("El alumno aún no tiene notas cargadas.")
            else:
                suma = 0
                for n in lista_notas:
                    suma = suma + n
                promedio = suma / len(lista_notas)
                print("El promedio de", apellido, "es:", promedio)
        else:
            print("El alumno no existe en el sistema.")
    elif opcion == "5":
        break

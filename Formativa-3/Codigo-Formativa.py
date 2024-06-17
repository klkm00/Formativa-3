
CARGOS = ['ceo','desarrollador','analista de datos']

trabajadores = []

def registrar_trabajador(trabajadores):
    print("↪ Ingrese los datos correspondientes")
    nombre = input("Nombre del trabajador:")
    apellido = input ("Apellido del trabajador:")
    cargo = input("Cargo del trabajador (CEO / Desarrollador / Analista de datos):").lower()
    while cargo not in CARGOS:
        cargo = input("Cargo del trabajador (CEO / Desarrollador / Analista de datos):").lower()
        sueldo = int(input("Sueldo bruto del trabajador:"))

    desc_salud = sueldo *0.07
    desc_afp = sueldo*0.12

    liquido = sueldo - desc_salud - desc_afp

    trabajadores.append({
        'Nombre:' : nombre : apellido
        'Cargo:' : cargo
        'Sueldo Bruto' : sueldo
        'Descuento Salud' : desc_salud
        'Descuento AFP' : desc_afp
        'Liquido a pagar' : liquido
    })

def listar_trabajadores(trabajadores):
    print("LISTA DE TRABAJADORES")
    for trabajador in trabajadores:
        print(trabajador)

def planilla_sueldos():
   seleccion = input("Cargo a imprimir planilla (CEO / Desarrollador / Analista de datos / Todos): ").lower()
   if seleccion == "todos":
        imprimir = trabajadores
        archivo_txt = 'planilla_todos.txt'
   elif seleccion in CARGOS:
        imprimir = []
        for trabajador in trabajadores:
            if trabajador['Cargo'] == seleccion:
                imprimir.appnd(trabajador)
        archivo_txt = f'planilla_{seleccion}.txt'
    else:
        print("Cargo invalido. Vuelva a intentarlo.")
        return


    with open(archivo_txt, 'w') as archivo:
        for trabajador in imprimir:
            archivo.write(f"Nombre y Apellido: {trabajador['Nombre']}\n")
            archivo.write(f"Cargo: {trabajador['Cargo']}\n")
            archivo.write(f"Sueldo Bruto: {trabajador['SueldoBruto']}\n")
            archivo.write(f"Descuento Salud: {trabajador['DescSalud']}\n")
            archivo.write(f"Descuento AFP: {trabajador['DescAFP']}\n")
            archivo.write(f"Liquido a Pagar: {trabajador['LiquidoPagar']}\n\n")


            
def menu():
    while True:
        print("MENU")
        print("1. Registrar trabajador")
        print("2. Listar todos los trabajadores")
        print("3. Imprimir planilla de sueldos")
        print("4. Salir del programa")
        try:
            opcion = int(input("Ir a: "))
        except ValueError:
            print("Opcion no valida. \n Debe ingresar una opcion entre 1 y 4.")
        
        if opcion == 1:
            registrar_trabajador(trabajadores)
        elif opcion == 2:
            listar_trabajadores(trabajadores)
        elif opcion == 3:
            planilla_sueldos(trabajadores)
        elif opcion == 4:
            print("Saliendo del programa.")
            break
        else:
            print("Opcion no valida. \n Debe ingresar una opcion entre 1 y 4.")
        
menu()



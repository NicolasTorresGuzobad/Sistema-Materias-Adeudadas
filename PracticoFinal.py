class Profesor:
    def __init__(self, nombre, materia, curso, division):
        self.nombre = nombre
        self.materia = materia
        self.curso = curso
        self.division = division

class Inscripcion:
    def __init__(self, fecha, alumno, materia, profesor,curso,division,nota):
        self.fecha = fecha
        self.alumno = alumno
        self.materia = materia
        self.profesor = profesor
        self.curso = curso
        self.division = division
        self.nota = nota

class Encargado:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

class Sistema:
    def __init__(self):
        self.profesores = []
        self.inscripciones = []
        self.encargados = []

    def cargar_profesores_desde_archivo(self,nombre_archivo):
        
        try:
            with open(nombre_archivo, 'r') as archivo:
                lineas = archivo.readlines()
                for linea in lineas:
                    campos = linea.strip().split(',')
                    if len(campos) == 4:  # Verifica si hay 4 campos (nombre, materia, curso, división)
                        nombre, materia, curso, division = campos
                        profe = Profesor(nombre, materia, curso, division)
                        self.profesores.append(profe)
                    else:
                        print(f"Error: línea no válida en el archivo {nombre_archivo}: {linea}")
        except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no se encuentra.")

    def get_profesores(self):
        return self.profesores
    
    def cargar_encargados_desde_archivo(self,nombre_archivo):
    
        try:
            with open(nombre_archivo, 'r') as archivo:
                lineas = archivo.readlines()
                for linea in lineas:
                    campos = linea.strip().split(',')
                    if len(campos) == 2:  # Verifica si hay 2 campos (nombre, dni)
                        nombre, dni = campos
                        en = Encargado(nombre, dni)
                        self.encargados.append(en)
                    else:
                        print(f"Error: línea no válida en el archivo {nombre_archivo}: {linea}")
        except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no se encuentra.")

    def get_encargados(self):

        return self.encargados    

    def cargar_inscripciones_desde_archivo(self,nombre_archivo):
    
        try:
            with open(nombre_archivo, 'r') as archivo:
                lineas = archivo.readlines()
                for linea in lineas:
                    campos = linea.strip().split(',')
                    if len(campos) == 7:  # Verifica si hay 2 campos (nombre, dni)
                        fecha, nombre_alumno, nombre_materia, nombre_profesor, curso, division, nota= campos
                        inscripcion = Inscripcion(fecha, nombre_alumno, nombre_materia, nombre_profesor, curso, division, nota)
                        self.inscripciones.append(inscripcion)
                    else:
                        print(f"Error: línea no válida en el archivo {nombre_archivo}: {linea}")
        except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no se encuentra.")

    def get_inscripciones(self):
        return self.inscripciones

    def inscribir_alumno(self, fecha, alumno, materia, profesor, curso, division, nota):
        inscripcion = Inscripcion(fecha, alumno, materia, profesor, curso, division, nota)
        self.inscripciones.append(inscripcion)

    def exportar_inscripciones_a_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'w') as archivo:
                for inscripcion in self.inscripciones:
                    linea = (
                        f"{inscripcion.fecha},"
                        f"{inscripcion.alumno},"
                        f"{inscripcion.materia},"
                        f"{inscripcion.profesor},"
                        f"{inscripcion.curso},"
                        f"{inscripcion.division},"
                        f"{inscripcion.nota}\n"
                    )
                    archivo.write(linea)
            print(f"Inscripciones exportadas correctamente a {nombre_archivo}")
        except Exception as e:
            print(f"Error al exportar inscripciones: {str(e)}")
        


gate = False

sistem = Sistema()
sistem.cargar_profesores_desde_archivo('Profesores.txt')
sistem.cargar_encargados_desde_archivo('Encargados.txt')
sistem.cargar_inscripciones_desde_archivo('Inscripciones.txt')

entrada = input(str('Coloque 1 si usted es un profesor o 2 si es un encargado: '))

if entrada == "1":
        
        nombreP = str(input("Ingrese su nombre: ")).lower().title()
        materiaP = str(input("Ingrese la materia que usted da: ")).lower().title()
        cursoP = str(input("Ingrese el curso donde da la materia: "))
        divisionP = str(input("Ingrese la division del curso: ")).upper()
        for profesor in sistem.get_profesores():
            if profesor.nombre == nombreP and profesor.materia == materiaP and profesor.curso == cursoP and profesor.division == divisionP:
                gate = True
                guardarNombre = nombreP
        if not gate:
            print ("Los datos ingresados son incorrectos")

elif entrada == "2":
    
    nombreEncargado = str(input("Ingrese su nombre: ")).lower().title()
    dniEncargado = str(input("Ingrese su DNI: "))

    for encargado in sistem.get_encargados():
        if encargado.nombre == nombreEncargado and encargado.dni == dniEncargado:
            gate = True
    if not gate:
        print ("Los datos ingresados son incorrectos")

elif entrada != "1" and entrada != "2":
    print ("Caracter incorrecto, vuelva a intentar")

while gate:
    print('\nMenu de opciones')
    print('Inserte 1 para realizar/modificar/eliminar una inscripcion de un estudiante')
    print('Inserte 2 para ingresar/eliminar la nota de un estudiante')
    print('Inserte 3 para cerrar el programa')

    menuDeOpciones = str(input("Selecione una opcion: "))
    
    if menuDeOpciones != "1" and menuDeOpciones != "2" and menuDeOpciones != "3":
        print("Opcion no encontrada, vuelva a intentar")
    
    elif menuDeOpciones == "1":
        print('\nMenu de inscripciones')
        print('Inserte 1 para realizar una inscripcion')
        print('Inserte 2 para modificar una inscripcion')
        print('Inserte 3 para eliminar una inscripcion')
        print('Si inserta un valor distinto se procedera al menu de opciones')

        opcionesIngreso = str(input("Seleccione una opcion: "))
        if opcionesIngreso != "1" and opcionesIngreso != "2" and opcionesIngreso != "3":
            print("Opcion no encontrada, volviendo al menu de opciones")
        
#Realizar inscripcion
        elif opcionesIngreso == "1":
            fecha = str(input("coloque la fecha con un formato DD/MM/YY: "))
            nombreAlumno = str(input("Coloque el nombre del alumno: ")).lower().title()
            materia = str(input("coloque el nombre de la materia: ")).lower().title()
            nombreProfesor = str(input("Coloque el nombre del profesor: ")).lower().title()
            curso = str(input("Coloque el curso: "))
            division = str(input("Coloque la division: ")).upper()
            nota = '-1'
            
            sistem.inscribir_alumno(fecha, nombreAlumno, materia, nombreProfesor, curso, division, nota)
        
#Modificar inscripcion
        elif opcionesIngreso == "2":
            nombreAlumno = str(input("Coloque el nombre del alumno: ")).lower().title()
            materia = str(input("Coloque el nombre de la materia: ")).lower().title()
    
            inscripcion_encontrada = None
            for inscripcion in sistem.get_inscripciones():
                if inscripcion.alumno == nombreAlumno and inscripcion.materia == materia:
                    inscripcion_encontrada = inscripcion
                    break

            if inscripcion_encontrada:
                print("Datos de inscripción:")
                print(f"Fecha: {inscripcion_encontrada.fecha}")
                print(f"Profesor: {inscripcion_encontrada.profesor}")
                print(f"Curso: {inscripcion_encontrada.curso}")
                print(f"División: {inscripcion_encontrada.division}")
                print(f"Nota actual: {inscripcion_encontrada.nota}")

                datoACambiar = input("¿Qué dato desea modificar (fecha/alumno/curso/división/profesor/materia)? ").lower()
                modificacion = input("Coloque el nuevo valor para el campo seleccionado: ")

                if datoACambiar == "fecha":
                    inscripcion_encontrada.fecha = modificacion
                elif datoACambiar == "alumno":
                    inscripcion_encontrada.alumno = modificacion.lower().title()
                elif datoACambiar == "curso":
                    inscripcion_encontrada.curso = modificacion.upper()
                elif datoACambiar == "división":
                    inscripcion_encontrada.division = modificacion
                elif datoACambiar == "profesor":
                    nombre_profesor = modificacion.lower().title()           
                elif datoACambiar == "materia":
                    inscripcion_encontrada.materia = modificacion.lower().title()
                else:
                    print("Opción no válida.")
            else:
                print("No se encontró la inscripción para el alumno y materia especificados.")
            
#Eliminar inscripcion
        elif opcionesIngreso == "3":
            nombreAlumno = str(input("Coloque el nombre del alumno: ")).lower().title()
            materia = str(input("Coloque el nombre de la materia: ")).lower().title()

            inscripcion_encontrada = None
            for inscripcion in sistem.get_inscripciones():
                if inscripcion.alumno == nombreAlumno and inscripcion.materia == materia:
                    inscripcion_encontrada = inscripcion
                    break

            if inscripcion_encontrada:
                sistem.get_inscripciones().remove(inscripcion_encontrada)
                print("Inscripción eliminada correctamente.")
            else:
                print("No se encontró la inscripción para el alumno y materia especificados.")

    elif menuDeOpciones == "2":
        print('\nMenu de calificaciones')
        print('Ingrese 1 para ingresar o modificar la nota')
        print('Ingrese 2 para eliminar la nota')
        print('Si inserta un valor distinto se procedera al menu de opciones')
        
        opcionesNota = str(input("Seleccione una opcion: "))
        if opcionesNota != "1" and opcionesNota != "2":
            print("Opcion no encontrada, volviendo al menu de opciones")

#Modificar nota
        elif opcionesNota == "1":
            nombreAlumno = str(input("Coloque el nombre del alumno: ")).lower().title()
            materia = str(input("Coloque el nombre de la materia: ")).lower().title()
            
            inscripcion_encontrada = None
            for inscripcion in sistem.get_inscripciones():
                if inscripcion.alumno == nombreAlumno and inscripcion.materia == materia and inscripcion.profesor == guardarNombre:
                    inscripcion_encontrada = inscripcion
                    break
            if inscripcion_encontrada:
                nueva_nota = input("Coloque la nueva nota del alumno: ")  # No es necesario convertirla a minúsculas
                inscripcion_encontrada.nota = nueva_nota
                print("Nota modificada correctamente.")
            else:
                print("No se encontró la inscripción para el alumno y materia especificados.")

#Eliminar nota
        elif opcionesNota == "2":
            
            nombreAlumno = str(input("Coloque el nombre del alumno: ")).lower().title()
            materia = str(input("coloque el nombre de la materia: ")).lower().title()
            
            for inscripcion in sistem.get_inscripciones():
                if inscripcion.alumno == nombreAlumno and inscripcion.materia == materia:
                    inscripcion.nota = -1
#Cerrar el programa
    elif menuDeOpciones == "3":
        gate = False
        sistem.exportar_inscripciones_a_archivo('Inscripciones.txt')









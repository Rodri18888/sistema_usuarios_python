from validaciones import validacion_datos, validacion_buscar_id

#Diccionario para guardar usuarios
dicc_usuarios = {}

#Variable para buscar id
id_buscar = 0

#Clase usuario
class Usuario:
    def __init__(self, id, nombre, apellido, edad, ciudad):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ciudad = ciudad

#Funcion para registrar usuarios
def registro_usuarios(id, nombre, apellido, edad, ciudad):
    try:
        validacion_datos(id, nombre, apellido, edad, ciudad)

        if id in dicc_usuarios:
            print(f"El ID {id} ya esta registrado")
            return None

        nuevo_usuario = Usuario(id, nombre.strip(), apellido.strip(), edad, ciudad.strip())
        dicc_usuarios[id] = nuevo_usuario
        print(f"El usuario {nombre} fue registrado correctamente")
        return nuevo_usuario
    except ValueError as error:
        print(f"Error de validacion: {error}")
        return None

#Funcion para listar usuarios
def listado_usuarios():
    for id_usuario, objeto_persona in dicc_usuarios.items():
        print(f"ID: {id_usuario} - Nombre: {objeto_persona.nombre} - Apellido: {objeto_persona.apellido} - Edad: {objeto_persona.edad} - Ciudad: {objeto_persona.ciudad}")
        
#Funcion para buscar usuarios
def buscar_usuario():
    try:   
        id_buscar = int(input("Ingrese la ID que desee buscar: ")) 
        validacion_buscar_id(id_buscar)

        for id_usuario, objeto_persona in dicc_usuarios.items():
            if id_buscar == id_usuario:
                print("Usuario encontrado:")
                print(f"ID: {id_usuario} - Nombre: {objeto_persona.nombre} - Apellido: {objeto_persona.apellido} - Edad: {objeto_persona.edad} - Ciudad: {objeto_persona.ciudad}")
                return
            else:
                print("Usuario no encontrado.")
                return    
    except ValueError as error:
        print(f"Error de validacion: {error}")
        return None




registro_usuarios(1, "Ana", "Ana", 18, "Medellin")
registro_usuarios(2, "Pepe", "fsdfds", 54, "Medellin")

buscar_usuario()
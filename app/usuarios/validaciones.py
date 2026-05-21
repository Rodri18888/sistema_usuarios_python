def validacion_datos(id, nombre, apellido, edad, ciudad):
    if not isinstance(id, int) or id <= 0:
        raise ValueError("El ID del usuario debe ser un numero entero")

    if not nombre or not nombre.strip():
        raise ValueError("El nombre no puede estar vacio")
    
    if not apellido or not apellido.strip():
        raise ValueError("El nombre no puede estar vacio")
    
    if not isinstance(edad, int) or edad <= 0:
        raise ValueError("El ID del usuario debe ser un numero entero") 
     
    if edad < 18:
      raise ValueError("El usuario no puede ser menor de edad") 

    if not ciudad or not ciudad.strip():
        raise ValueError("La ciudad no puede estar vacia")  
     
    return True  


def validacion_buscar_id(id_buscar):
    if not isinstance(id_buscar, int) or id_buscar <= 0:
        raise ValueError("El ID a buscar debe ser un numero entero")
    
    return True

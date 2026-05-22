import app

# Crear objetos para probar
app.usuarios.registro_usuarios(1, "Ana", "Ana", 18, "Medellin")
app.usuarios.registro_usuarios(2, "Pepe", "Lopez", 54, "Medellin")
app.usuarios.registro_usuarios(3, "Roberto", "Perez", 14, "Medellin") #Menor de edad para probar validaciones
app.usuarios.registro_usuarios(-4, "Test", "Test", 54, "Test") #Id negativa para probar validaciones
app.usuarios.registro_usuarios(4, "Patricio", "Pedregal", 20, "Bogota")
app.usuarios.registro_usuarios(5, "Sofia", "fsdfds", 54, "Cartagena")
app.usuarios.registro_usuarios(4, "Patricio", "Pedregal", 20, "Bogota") #Id ya existente

#app.buscar_usuario()

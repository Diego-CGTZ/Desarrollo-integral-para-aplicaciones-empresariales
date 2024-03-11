import turtle #Se importa el modulo turtle para poder hacer los trazados.

window = turtle.Screen() #Se crea una ventana para poder ver los trazos.
tortuga = turtle.Turtle() #Se crea al objeto tortuga, que es el elmento con el que se interactua.

def trazarCuadrado(): #En esta funcion se traza un cuadrado.
    for i in range(4): #Contiene un ciclo que se repite cuatro veces para formar las cuatro caras.
        tortuga.left(90) #Giro de 90 grados.
        tortuga.forward(100) #Avance de 100px.

def trazarTriangulo(): #En esta funcion se traza el triangulo.
    for i in range(3): #Contiene un ciclo que se repite 3 veces para formar las tres caras.
        tortuga.left(120) #Giro de 120 grados.
        tortuga.forward(100) #Avance de 100px.

def trazarPentagono(): #En esta funcion se traza el pentagono.
    for i in range(5): #Contiene un ciclo que se repite 5 veces para formar las cinco caras.
        tortuga.left(72) #Giro de 120 grados.
        tortuga.forward(100) #Avance de 100px.

trazarPentagono() #En esta seccion se llaman todas las funciones para dibujar la figura.
trazarCuadrado()
trazarTriangulo()

window.mainloop() #Es un bucle de eventos infinitos que se termina cuando el usuario cierra la aplicación.

import turtle #Se importa el modulo turtle para poder hacer los trazados.

window = turtle.Screen() #Se crea una ventana para poder ver los trazos.
tortuga = turtle.Turtle() #Se crea al objeto tortuga, que es el elmento con el que se interactua.

for i in range (3): #Ciclo que se encarga de girar 22.5° a tortuga cada que se cumple con el ciclo anidado.
    tortuga.left(22.5) #Giro de 22.5°.
    for i in range(4): #Ciclo anidado que se repite 4 veces para hacer las cuatro caras del cuadrado.
        tortuga.forward(100) #Avance de 100px.
        tortuga.left(90) #Giro de 90°.
    
window.mainloop() #Es un bucle de eventos infinitos que se termina cuando el usuario cierra la aplicación.
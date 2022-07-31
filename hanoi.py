ant = ["123", "", ""]
act = ["", "", ""]
continuar = True

###
#   En este ejercicio vamos a ver todos los estados posibles de las Torres de Hanoi
#   La salida es una lista de 3 posiciones representando cada una de las torres    
#   En cada posición hay una cadena que puede estar vacia o contener numeros
#   Cada numero representa un disco, sientod 3 el de mayor tamaño y 1 el mas pequeño
#   Las cadenas se leen de izquierda a derecha que representam los discos de arriba hacia abajo
###

while(continuar):
    if "1" in ant[0]:
        act[1] = act[1] + "1"
    if "1" in ant[1]:
        act[2] = act[2] + "1"
    if "1" in ant[2]:
        act[0] = act[0] + "1"
        if "2" in ant[0]:
            act[1] = act[1] + "2"
        if "2" in ant[1]:
            act[2] = act[2] + "2"
        if "2" in ant[2]:
            act[0] = act[0] + "2"
            if "3" in ant[0]:
                act[1] = act[1] + "3"
            if "3" in ant[1]:
                act[2] =act[2] + "3"
            if "3" in ant[2]:
                act[0] = act[0] + "3"
                continuar = False
        else:
            if "3" in ant[0]:
                act[0] = act[0] + "3"
            if "3" in ant[1]:
                act[1] =act[1] + "3"
            if "3" in ant[2]:
                act[2] =act[2] + "3"
    else:
        if "2" in ant[0]:
            act[0] = act[0] + "2"
        if "2" in ant[1]:
            act[1] = act[1] + "2"
        if "2" in ant[2]:
            act[2] = act[2] + "2"
        if "3" in ant[0]:
            act[0] = act[0] + "3"
        if "3" in ant[1]:
            act[1] = act[1] + "3"
        if "3" in ant[2]:
            act[2] = act[2] + "3"
            
    print(act)
    ant = act
    act = ["","",""]
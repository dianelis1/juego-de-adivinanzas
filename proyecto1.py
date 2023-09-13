import random
import math
límite_inferior=float(input('Por favor ingresa un número,que será el límite inferior del rango: '))
límite_superior=float(input('Por favor ingresa un número,que será el límite superior del rango: '))
número_aleatorio=random.randint(límite_inferior,límite_superior)
número_mínimo_de_conjeturas = round(math.log2(límite_superior - límite_inferior + 1))
print('Tienes solo %d intentos.'%número_mínimo_de_conjeturas)
contador=0
while True:
    entrada=(input('Por favor ingresa un número para adivinar: '))
    try:
        número=float(entrada)
        contador += 1
        if número==número_aleatorio:
           print('Felicitaciones')
           print('Lo adivinaste en: ',contador)
           break
        elif número > número_aleatorio:
           print("¡ Inténtalo de nuevo!. Adivinaste demasiado alto") 
        elif número < número_aleatorio:
           print("¡ Inténtalo de nuevo!. Adivinaste demasiado pequeño") 
           
    except ValueError:
        print("No has ingresado un número válido. Inténtalo de nuevo.")
    if contador>=número_mínimo_de_conjeturas:
       print('Haz alcanzado el número máximo de intentos.Más suerte la próxima vez,el número era: ',número_aleatorio)
       break

       

    
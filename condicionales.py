# Declaramos una variable
calificacion = input("Introduce tu calificacion de la AZ-900: ")

calificacion = int(calificacion)


# Preguntamos si la calificacion es menor a 700
if calificacion < 700 : 
    print("Veeeees, por no estudiar") # Si es menor a 700, muestra esto
elif calificacion > 1000 :
    print(" mientes!!! no puedes sacar mas de 1000")
else :
    print(" Felicidades, pasa por tu certificado")

# Verificador de mayoria de edad
edad = input("Introduce tu edad: ")
edad = int(edad)

if edad >= 18 and edad <= 100 : 
    print("Bienvenid@ al mamitas")
elif edad > 100 :
    print("Si vienes acompañado de tus abuelitos , si te podemos fiar")
elif edad < 0 :
    print("Ni que fueras viajero del tiempo")
else : 
    print("No puedes llevarte esos cigarros")

# En python no hay switch case
# Estructuras condicionales:
# Son aquellas que permiten ejecutar determinadas 
# partes del código según se cumpla o no cierta condición.

# Ejemplo: Se solicita al usuario que ingrese su edad 
# y se imprimira un mensaje dependiendo del valor ingresado.

# Si / if

print("Ingresa un tu edad:")
edad = int(input())

if edad >= 18:
    print("Sos mayor de edad")


# SINO / if ... else

print("Ingresa un tu edad:")
edad = int(input())

if edad >= 18:
    print("Sos mayor de edad")
else:
    print("Sos menor de edad")


# SINO SI / if ... elif ... else

print("Ingresa un tu edad:")
edad = int(input())

if edad >= 18:
    print("Sos mayor de edad")
elif edad >= 16:
    print("Sos menor pero podes votar")
else:
    print("Sos menor de edad")

# Estructuras repetitivas:
# Son aquellas que permiten ejecutar varias veces
# un determinado bloque de codigo mientras se cumpla una condicion.

# Ejemplo: Cantidad de intentos para ingresar una contraseña correcta.

# MIENTRAS / while
# Suponemos que no existen restricciones de intentos para la clave correcta,
# entonces el usuario podra intentar ingresar la cantidad de veces que desee.
# Por lo que la ejecucion no finalizara hasta que se ingrese la clave esperada.

print("Ingresa tu contraseña:")
clave = input()
CLAVE_ESPERADA = "info2025"

while clave != CLAVE_ESPERADA:
    print("Contraseña incorrecta, ingresala nuevamente:")
    clave = input()
print("Contraseña correcta")

# PARA / for
# En este caso suponemos que solamente es posible intentar ingresar la clave,
# hasta 3 veces.

print("Ingresa tu contraseña:")
clave = input()

for i in range(1, 3):
    if clave == "info2025":
        print("Contraseña correcta")
        break
    
    print("Contraseña incorrecta, ingresala nuevamente:")
    clave = input()

# Agregando alguna validacion mas:

print("Ingresa tu contraseña:")
clave = input()
INTENTOS_POSIBLES = 3
CLAVE_ESPERADA = "info2025"
intento = 1

for i in range(1, INTENTOS_POSIBLES):
    if clave == CLAVE_ESPERADA:
        print("Contraseña correcta")
        break
    
    intento += 1
    print("Contraseña incorrecta, ingresala nuevamente:")
    clave = input()

if intento == INTENTOS_POSIBLES:
    print("Ya no tenes mas intentos posibles, cuenta bloqueada")

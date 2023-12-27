
# Anotaciones lenguaje Python

# Asignar multiples variables con el mismo valor 
x=y=z=5

# Desempaquetar una lista 
fruits = ["banana","apple","cherry"]
x,y,z = fruits

# Es posible convertir enteros a numeros complejos 
i = 5
c = complex(i)

# Operador ternario
edad = 13
if edad < 18:
	print('Eres menor de edad')
else:
	print('Eres mayor de edad')
# La manera de simplificar esto es asi

print('Eres menor de edad' if edad < 18 else 'Eres mayor de edad')


# Hay una forma de simplificar los if elif else con listas o diccionarios

if opcion == 1:
	login()
elif opcion == 2:
	registrarse()
elif opcion == 3:
	eliminar()
elif opcion == 4:
	actualizar()
else:
	salir()
# La manera de hacerlo rapido con un diccionario es la siguiente:

actions = {
	1: login,
	2: registrarse,
	3: eliminar,
	4: actualizar
}

if opcion in actions:
	actions[opcion]()
else:
	salir()

# Estructuras de datos
# Algunas estructuras son las Pilas y las Colas, lo primero que se te viene a la cabeza es usar una lista

nums = []
for num in range(100000):
	# Esto es rapido
	nums.append(num)

nums = []
for num in range(100000):
	# Esto es lento
	nums.insert(0,num)
# la solucion es usar una lista con doble entrada llamado deque
from collections import deque

mi_deque = deque()
for num in range(100000):	mi_deque.append(num)
for num in range(100000):	mi_deque.appendLeft(num)
for num in range(100000):	mi_deque.pop()
for num in range(100000):	mi_deque.popLeft()
# Existe una funcion dir() para imprimir todas las variables de un modulo
# Hay que estudiar las funciones dir(),eval(),all(),exec()



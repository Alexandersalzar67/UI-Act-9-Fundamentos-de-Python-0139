#Alexander Salazar NC = 0139
print("+-+-+-+-+-+-+-+-+-+")
print("ejemplo 1")
x = 5
y = "John"
print(x)
print(y)
print("+-+-+-+-+-+-+-+-+-+")
print("ejemplo 2")
a = 4
A = "Sally"
print(x)
print("+-+-+-+-+-+-+-+-+-+")
print("ejemplo 3")
x = "John"
# is the same as
x = 'John'


print("Variables de Python: Asignar múltiples valores")
print("ejemplo 1")
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
print("+-+-+-+-+-+-+-+-+-+")
print("ejemplo 2")
x = y = z = "Orange"
print(x)
print(y)
print(z)
print("+-+-+-+-+-+-+-+-+-+")
print("ejemplo 3")
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


print("Tipos de datos de Python")
print("ejemplo 1")
str
numéricos:	int
secuencia:	list
mapeo:	dict
conjuntos:	set
booleano:	bool
binarios:	bytes

print("+-+-+-+-+-+-+-+-+-+")
print("ejemplo 2")
x = 5
print(type(x))
print("+-+-+-+-+-+-+-+-+-+")
print("ejemplo 3")
x = "Hello World"    	
x = 20		
x = 20.5		
x = 1j		
x = ["apple", "banana", "cherry"]		
x = ("apple", "banana", "cherry")		
x = range(6)		
x = {"name" : "John", "age" : 36}	
x = {"apple", "banana", "cherry"}	
x = frozenset({"apple", "banana", "cherry"})	
x = True		
x = b"Hello"	
x = bytearray(5)		
x = memoryview(bytes(5))		
x = None


print("Operadores aritméticos de Python")	
print("ejemplo 1")
x + y	
x * y	
x / y	
x % y	
x ** y	
x // y	
print("+-+-+-+-+-+-+-+-+-+")
print("ejemplo 2")
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)
x = 15
y = 4
print("+-+-+-+-+-+-+-+-+-+")
print("ejemplo 3")
x = 12
y = 5

print(x / y)
x = 12
y = 5

print(x // y)
print("Operadores de comparación en Python")	
print("ejemplo 1")
x == y	
x = y	
x > y	
x < y	
x >= y	
x <= y	
print("+-+-+-+-+-+-+-+-+-+")
print("ejemplo 2")
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print("+-+-+-+-+-+-+-+-+-+")
print("ejemplo 3")
x = 5

print(1 < x < 10)

print(1 < x and x < 10)
print("Operadores lógicos de Pythom")	
print("ejemplo 1")
x < 5 and  x < 10	
x < 5 or x < 4	
(x < 5 and x < 10)
print("+-+-+-+-+-+-+-+-+-+")
print("ejemplo 2")
x = 5

print(x < 5 or x > 10)
print("+-+-+-+-+-+-+-+-+-+")
print("ejemplo 3")
x = 5

print(not(x > 3 and x < 10))
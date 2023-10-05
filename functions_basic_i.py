#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# Predicción: Va a imprimir 5
# Resultado: Imprime 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# Predicción: Imprimirá un 5
# Resultado: Se genera un error pues la primera función llamada no existe

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# Predicción: Devolverá un 5
# Resultado: Devuelve un 5
#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# Predicción: Se imprimirá un 5
# Resultado: Se imprime un 5

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# Predicción: El llamado a la función al asignarla a x imprimirá un 5 y no se imprimirá nada más ya que x no tiene un valor asignado
# Resultado: Se imprime 5 y se genera un error porque x no tiene valor asignado

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# Predicción: Los llamados a las funciones en print imprimirán 3 y 5 respectivamente. Pero no imprimirá nada más porque add no devuelve valores
# Resultado: Los llamados a las funciones imprimieron 3 y 5 y hubo un error porque add no devuelve valores

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# Predicción: Se imprimirá una concatenación entre los dos valores así: 25
# Resultado: Imprime 25

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# Predicción: Se imprimirá un 100 y luego un 10
# Resultado: Se imprime un 100 y un 10

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# Predicción: Se imprime un 7, luego un 14 y luego un 21
# Resultado: Se imprimen 7, 14 y 21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# Predicción: Se imprime un 8
# Resultado: Se imprime 8

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# Predicción: Se imprime 500, 500, 300 y 500
# Resultado: Se imprime 500, 500, 300, 500

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# Predicción: Se imprime 500, 500, 300 y 500
# Resultado: Se imprime 500, 500, 300, 500

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# Predicción: Se imprime 500, 500, 300, 300
# Resultado: Se imprime 500, 500, 300, 300

def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# Predicción: Se imprime 1, 3 y 2
# Resultado: Se imprime 1, 3 y 2

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# Predicción: Se imprime 1, 3, 5 y 10
# Resultado: Se imprime 1, 3, 5 y 10
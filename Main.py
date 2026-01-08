# Main.py criada em 2025-02-05

# Quero criar uma função que calcule a soma e o produto de dois números
a = 5
b = 10
soma = 'Cachorro'
produto = 'Gato'
def calcular_soma_e_produto(a, b):
    global soma, produto
    soma = a + b
    produto = a * b
calcular_soma_e_produto(a, b)
print('Soma:', soma)
print('Produto:', produto)


# Consider the following code:
x = 'Bruno'
y = 'Carlos'
def myfunc():
    global x, y
    x = 'Mariana'
    y = 'Ana'
myfunc()
print('Python is ' + x)


import random

print(random.randrange(1, 10))

for i in range(10):
    print(i)
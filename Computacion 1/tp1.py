#1 – Imprimir “Hola mundo” por pantalla
print("Hola mundo")

#2 - Crear dos variables numéricas, sumarlas y mostrar su resultado.
a = 1;
b = 2;
c = a + b;
print(c)

#3 – Mostrar el iva de un producto con un precio de 200, y su precio final.

prduct = 200;
iva = 21;

product_with_iva = prduct * iva;
product_iva = product_with_iva / 100;
product_final = product_iva + 200;

print(product_final)

#4 – de dos números, saber cual es el mayor.

a = 3;
b = 2;

if a > b :
    print(a, " es mayor que ",b);
elif a < b:
    print("a es menor que b");
else:
    print("los numeros son iguales");
#5 – crear una variable numérica, he indicar si esta entre 0 y 10.
a = 2;

if a <= 10:
    print("es menor o igual que 10");
else:
    print("es mayor que 10");

#6 – añadir al ejercicio anterior si la variable esta entre 11 y 20, o entre 21 y 30.
a = 22;

if a <= 10:
    print("es menor o igual que 10");
elif a >= 11 and a <= 20 :
    print("esta entre 11 y 20");
elif a >= 21 and a <= 30 :
    print("esta entre 21 y 30");
else:
    print("el numero es invalido");

#7 – mostrar con un while los números entre 1 y 50.
i = 1;

while i != 50:
    i += 1
    #print(i)

#8 – mostrar con un for los números entre 1 y 50.
    
x = 1;
for x in range(50):
    x += 1
    print(x);

#9 – mostrar los caracteres de la cadena “Hola mundo”
a = 'hola mundo';
for caracteres in a:
    print(caracteres);



#10 – mostrar los números pares entre 1 y 100.
a = 2;
while a <= 100:
    print(a)
    a += 2
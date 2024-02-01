#1
n=6
def ej_1 (n):
    result = n * 2;
    return print(result);

ej_1(n)

#2

def ej_2 (string):
    large = len(string);
    return print(large)
string = "test";
ej_2(string)


#3

def ej_3 (num1,num2):
    resul3 = num1 * num2;
    return print("el resultado del ej 3 es: ",resul3);

num1 = 2;
num2 = 3;
ej_3(num1,num2)

#4

def ej_4 (list):
    result4 = sum(list);
    return print(result4)

list = [1,2,3]
ej_4(list)

#5

def ej_5(chain):
    return chain[::-1]

chain1 = "Hola, mundo!"
chain_inverted = ej_5(chain1)

print(f"Cadena original: {chain1}")
print(f"Cadena invertida: {chain_inverted}")

#6	Escribir una función que tome una lista de números como argumento y devuelva una nueva lista con todos los números pares de la lista original.

def ej_6(lista_numeros):
    numeros_pares = [numero for numero in lista_numeros if numero % 2 == 0]
    return numeros_pares

lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_pares = ej_6(lista_original)

print(f"Lista de números pares: {lista_pares}")

#7

def ej_7(list_numbers):
    result = sorted(list_numbers);
    return print(result)

list_numbers = [111,22,333,41,52]
ej_7(list_numbers)

#8

def invertir_palabras(cadena):
    palabras = cadena.split()  
    palabras_invertidas = [palabra[::-1] for palabra in palabras]
    cadena_invertida = ' '.join(palabras_invertidas)
    return cadena_invertida

cadena_original = "Hola mundo a la perinola"
cadena_invertida = invertir_palabras(cadena_original)

print(f"Cadena con palabras invertidas: {cadena_invertida}")

#9

def elementos_comunes(lista1, lista2):
    result9 = (set(lista1) & set(lista2));
    return print(result9)

# Ejemplo de uso
lista_a = [1, 2, 3, 4, 5]
lista_b = [4, 5, 6, 7, 8]

comunes = elementos_comunes(lista_a, lista_b)

#10

#menu
print("Bienvenido a nuestro calculador de impuestos:")

def menu(option):
    if option == 1:
        product = int(input("Ingrese el valor de su producto: "))
        calculo_1 = product * 8;
        calculo_2 = calculo_1 / 100;
        resultado = calculo_2 + product;
        print("lo que vale tu producto con el iva incluido es:",resultado)
    elif option == 2:
        ventas = str(input("Usted vende productos al exterior? (1 para si / 2 para no) :"))
        if ventas == 1:
            print("usted no paga iva")
        elif ventas == 2:
            product = int(input("Ingrese el valor de su producto: "))
            calculo_1 = product * 16;
            calculo_2 = calculo_1 / 100;
            resultado = calculo_2 + product;
            print("usted paga: ",resultado)
        else:
            print("usted ingreso una opcion icorrecta")
            return ventas
    elif option == 3:
        product = int(input("Ingrese el valor de su producto: "))
        calculo_1 = product * 21;
        calculo_2 = calculo_1 / 100;
        resultado = calculo_2 + product;
        print("lo que vale tu producto con el iva incluido es:",resultado)
    elif option == 4:
        print("Adios");
        exit;
    else:
        print("respuesta invalida")

option = int(input("Ingrese 1 si es de USA, 2 si es de México, 3 si es de Argentina, 4 para salir: "));
menu(option)

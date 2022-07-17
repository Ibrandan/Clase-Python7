print("Error de sintaxis")
# print("hola" #----> IndexError : Al leer el archivo encontro un enter en ves de un parentesis


print("Error de nombre")
# pint("hola") #----> IndexError : La funcion pint no esta definida


print("Errores semanticos")
l = []  # ------> Lista vacia
# l.pop() ------> IndexError : Al estar la lista vacia no podemos sacar ningun elemento mediante el pop
if len(l) > 0:  # ----> Para asegurarnos de que el programa no tenga errores deberiamos verificar la longitud de la lista
    l.pop()      # -----> Ejecuta el po solo si la lista tiene al menos un elemento

n = input("Introduce un numero")  # Siempre retorna str
m = 4
# print("{ }/{ } = { }".format(n, m, n / m)) # ----> TypeError: No podemos dividir un str con un int

# ----> Para solucionar el TypeError usamos el float para conventir el resultado del input a real
n = float(n)
print("{ }/{ } = { }".format(n, m, n / m))

# Uso de format
formatted_String = "Hola soy {}, tengo {} años".format("Ignacio", 18)
print(formatted_String)

print("Excepciones")

# Try except

try:
    n = float(input("Introduce un numero: "))
    m = 4
except:  # Si el usuario no ingresa un numero, se ejecuta el except
    print("Ha ocurrido un error, introduce un numero valido")

# ---> Si el usuario ingresa un numeor, luego el programa sigue con exito
print("Continuo la ejecucion")

# La forma correcta para que no haya errores es usando bucles
while True:
    try:
        n = float(input("Introduce un numero: "))
        m = 4
        print("{ }/{ } = { }".format(n, m, n / m))
        break
    except:
        print("Ha ocurrido un error, introduce un numero valido")

# Con un else
while True:
    try:
        n = float(input("Introduce un numero: "))
        m = 4
        print("{ }/{ } = { }".format(n, m, n / m))
    except:
        print("Ha ocurrido un error, introduce un numero valido")
    else:
        print("Todo ha funciona correctamente")
        break
    finally:
        # Se ejecuta siempre, haya habido o no excepcion
        print("Fin de la iteracion")

# Ejemplo del uso del finally
myFile = open("test.txt", "w")

try:
    myFile.write("the answer is: ")
    myFile.write(42)  # Devuelve un type error
finally:
    # Se cierra el archivo haya habido excepcion o no
    myFile.close()

# Exception contiene todos los tipos de errores
# ValueError, TypeError, SyntaxError, etc. Son hijas de exception

try:
    n = input("introduce un numero: ")
    5/n  # ---> ValueError
except Exception as e:
    # Devuelve el tipo de error
    print("Ha ocurrido un error =>", type(e).__name__)

print(type(1).__name__)  # imprime el nombre del tipo de dato sin <class "">
print(type(3.14).__name__)

try:
    n = float(input("Introduce un numero divisor: "))
    5/n
except TypeError:  # Cuando ocurre un typeError hace lo siguiente
    print("No se puede dividir el numero entre una cadena")
except ValueError:  # Cuando ocurre un ValueErro hace lo siguiente
    print("Debes introducir una cadena que sea un numero")
except ZeroDivisionError:  # Cuando ocurre un ZeroDivisionError hace lo siguiente
    print("No se puede dividir por 0")
except Exception as e:  # Es importante la ubicacion, debemos poner del mas especifico al menos especifico
    print("Ha ocurrido un error no  previsto")

# Excepciones propias


def mi_funcion(algo=None):
    if algo is None:
        print("Error! no se permite un valor nulo ")  # ----> Con un print


mi_funcion()  # Al llamar a la funcion sin parametros devuelve el error creado


def mi_funcion(algo=None):
    try:
        if algo is None:
            # raise es una palabra reservada, sirve para mostrar excepciones
            raise MyError("Error! no se permite un valor nulo")
    except MyError:
        print("Error!")


class MyError(Exception):
    def __init__(self, massage):
        self.message = massage


mi_funcion()


import pandas as pd

# donde esta el problema de este ejercicio?
pago_cuentas = [
    {'nombre': 'AGUAS ALTIPLANO', 'valor': 90},
    {'nombre': 'AGUAS ARAUCANIA', 'valor': 183},
    {'nombre': 'AGUAS MAGALLANES', 'valor': 17},
    {'nombre': 'BELCORP ESIK/LB', 'valor': 84},
    {'nombre': 'CLARO', 'valor': 264},
    {'nombre': 'DIRECTV MENSUAL', 'valor': 236},
    {'nombre': 'ENTEL PCS', 'valor': 2586},
    {'nombre': 'FONASA', 'valor': 873},
    {'nombre': 'EF SECURITIZADORA SA', 'valor': 72},
    {'nombre': 'MOVISTAR', 'valor': 3547},
    {'nombre': 'MUNDO PACIFICO', 'valor': 432},
    {'nombre': 'VTR', 'valor': 779},
    {'nombre': 'WOM', 'valor': 2795}
]


def agregar_producto():
    try:
        print("Agregar Producto")
        cuenta = input("Ingrese el producto: \n")
        valor = float(input("Ingrese el precio: \n"))
        pago_cuentas.append({"producto": cuenta, "precio": valor})
        print("la cuenta fue agregada exitosamente. \n")
    except ValueError:
        print("Favor ingrese un producto válido.")



def eliminar_pago():
    try:
        cuenta = input("Ingrese el producto a eliminar: \n").lower()
        for item in pago_cuentas[:]:  # iterate over a copy of the list
            if item["nombre"].lower() == cuenta:  # assuming the product name is in the "nombre" key
                pago_cuentas.remove(item)
                print("la cuenta fue eliminada exitosamente \n")
                return
        print("Producto no encontrado.")
    except ValueError:
        print("Favor ingrese un producto válido.")



def quick_sort(lista):
    # Caso base: si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(lista) <= 1:
        return lista

    # Elegimos el primer elemento como "pivote"
    pivote = lista[0]

    # Lista de productos cuyo nombre es menor (en orden alfabético) al pivote
    menores = [x for x in lista[1:] if x ["nombre"].lower() < pivote["nombre"].lower()]

    # Lista de productos cuyo nombre es mayor o igual al pivote
    mayores = [x for x in lista[1:] if x["nombre"].lower() >= pivote["nombre"].lower()]
    
    # Llamamos recursivamente a quick_sort para ordenar 'menores' y 'mayores', y concatenamos todo
    return quick_sort(menores) + [pivote] + quick_sort(mayores)




def busqueda_binaria(lista, objetivo):
    # Definimos los extremos de la búsqueda
    izquierda, derecha = 0, len(lista) - 1

    # Mientras haya elementos en el rango a revisar
    while izquierda <= derecha:
        # Calculamos la posición del elemento medio
        medio = (izquierda + derecha) // 2
        nombre_medio = lista[medio]["nombre"].lower()

        # Comparamos el nombre del medio con el objetivo
        if nombre_medio == objetivo.lower():
            return lista[medio]  # Si es igual, encontramos el producto
        elif objetivo.lower() < nombre_medio:
            # Si el objetivo es menor, seguimos buscando en la mitad izquierda
            derecha = medio - 1
        else:
            # Si el objetivo es mayor, seguimos buscando en la mitad derecha
            izquierda = medio + 1

    # Si no encontramos el producto, devolvemos None
    return None



print("=========================")
print("           Menu          ")
print("=========================")
print("1. Agregar Pagos")
print("2. Revisar Pagos")
print("3. Eliminar Pagos")
print("4. Salir")
print("=========================")
while True:
    opcion= int(input('Ingrese una opcion:\n'))
    if opcion == 1:
         agregar_producto()
    elif opcion == 2:
         pass
    elif opcion == 3:
         eliminar_pago()
    elif opcion == 4:
         print("Saliendo del programa")
         break
    else:
         print("Opcion no valida")

#print(pago_cuentas)
#pago_cuentas = pd.DataFrame(pago_cuentas)


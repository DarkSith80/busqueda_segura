"""
Objetivo:
Desarrollar una aplicación de consola en Python que permita:
• Agregar productos a un inventario.
• Ordenar los pago_cuentas alfabéticamente y por precio.
• Buscar productos por tipo.
• Validar correctamente la entrada del usuario para proteger la aplicación.
"""
import pandas as pd

pago_cuentas = {
    "AGUAS ALTIPLANO": 90,
    "AGUAS ARAUCANIA": 183,
    "AGUAS MAGALLANES": 17,
    "BELCORP ESIK/LB": 84,
    "CLARO": 264,
    "DIRECTV MENSUAL": 236,
    "ENTEL PCS": 2586,
    "FONASA": 873,
    "EF SECURITIZADORA SA": 72,
    "MOVISTAR": 3547,
    "MUNDO PACIFICO": 432,
    "VTR": 779,
    "WOM": 2795
}

def agregar_producto():
    try:
        print("Agregar Producto")
        cuenta = input("Ingrese el producto: ")
        valor = float(input("Ingrese el precio: "))
        pago_cuentas.append({"producto": cuenta, "precio": valor})
        print("la cuenta fue agregada exitosamente.")
    except ValueError:
        print("Favor ingrese un producto válido.")

def ordenar_lista():
    if not pago_cuentas:
        print('la lista esta vacia.') # <-- si la lista está vacía, no se puede ordenar
    return sorted(pago_cuentas.items(), key=lambda x: x[0].lower()) # <-- ordenar por clave (nombre)


def busqueda_binaria(lista, nombre_buscado):
    izquierda = 0 # <-- índice inicial
    derecha = len(lista) - 1 # <-- índice final

    while izquierda <= derecha: # <-- mientras haya elementos en la lista
        medio = (izquierda + derecha) // 2 # <-- índice medio
        nombre_actual = lista[medio][0].lower() # <-- nombre del producto en la posición media

        if nombre_actual == nombre_buscado.lower(): # <-- si el nombre actual es igual al buscado
            return lista[medio]
        elif nombre_actual < nombre_buscado.lower(): # <-- si el nombre actual es menor que el buscado
            izquierda = medio + 1 # <-- el índice inicial se actualiza
        else:
            derecha = medio - 1 # <-- el índice final se actualiza

    return None # <--si no se encuentra el producto, se devuelve

def borrar_pago_cuenta():
    print('Borrar Cuenta')
    cuenta = input('Ingrese la cuenta que sea borrar:\n')



df = pd.DataFrame(pago_cuentas)  # <-- se convierte el diccionario en un DataFrame
print(df)



def ordenar_alfabeticamente():
    df.sort_values(by='producto', inplace=True) # <-- ordena el DataFrame por el campo 'producto'
    print(df)

'''
print("=============================")
print("         Menu                ")
print("=============================")
print("Bienvenido a la aplicación de gestión de cuentas")
print("1. Agregar una Cuenta")
print("2. Borrar una Cuenta")
print("3. Buscar una Cuenta")
print("4. Salir")
while True:
    try:
        opcion = int(input("Ingrese una Opcion:\n"))
        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            pass
'''





import pickle
import os
import time
from datetime import datetime

# Obtiene la ruta de la carpeta en la que se encuentra este script
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Especifica la ruta al archivo .pickle basado en la ubicación del script
archivo_pickle = os.path.join(directorio_actual, 'trader_state.pickle')

# Campos a excluir de la impresión
campos_a_excluir = {'Last_price', 'Current_close', 'Current_rsi'}

# Función para cargar y mostrar el contenido del archivo pickle con la fecha y hora
def mostrar_contenido(contenido):
    ahora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'\nContenido del archivo ({ahora}):')

    # Imprime el contenido para verlo, excluyendo los campos especificados
    for key, value in contenido.items():
        if key not in campos_a_excluir:
            print(f'{key}: {value}')

# Obtén la fecha de modificación inicial del archivo
def obtener_fecha_modificacion(archivo):
    return os.path.getmtime(archivo)

# Carga el contenido del archivo pickle
def cargar_contenido():
    with open(archivo_pickle, 'rb') as f:
        return pickle.load(f)

# Inicializa la fecha de modificación y contenido del archivo
fecha_modificacion_anterior = obtener_fecha_modificacion(archivo_pickle)
contenido_anterior = cargar_contenido()

# Realiza la primera impresión
mostrar_contenido(contenido_anterior)

# Ejecuta el ciclo para verificar cambios e imprimir cada 3 segundos
while True:
    time.sleep(5)

    # Obtén la fecha de modificación actual del archivo
    fecha_modificacion_actual = obtener_fecha_modificacion(archivo_pickle)

    # Si la fecha de modificación ha cambiado, revisa el contenido del archivo
    if fecha_modificacion_actual != fecha_modificacion_anterior:
        contenido_nuevo = cargar_contenido()

        # Comparar el contenido excluyendo los campos especificados
        cambios_detectados = any(
            key not in campos_a_excluir and contenido_anterior.get(key) != contenido_nuevo.get(key)
            for key in contenido_nuevo
        )

        if cambios_detectados:
            mostrar_contenido(contenido_nuevo)

        # Actualiza la fecha de modificación y el contenido anterior
        fecha_modificacion_anterior = fecha_modificacion_actual
        contenido_anterior = contenido_nuevo
